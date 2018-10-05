import re

from dateutil.relativedelta import relativedelta
from edc_constants.constants import UUID_PATTERN

from django.db import models
from edc_search.model_mixins import SearchSlugManager, SearchSlugModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin

from edc_base.utils import get_utcnow
from .choices import (GENDER, YES_NO, YES_NO_MC,
                      MARITAL_STATUS, ADDRESS, JOB_DETAILS,
                      JOB_DESCRIPTION, COMMUNITY_ACTIVITY,
                      JOB_INCOME, NEIGHBORHOOD_PROBLEMS,
                      YES_NO_DWTA, YES_NO_GP, YES_NO_LW, YES_NO_NA_DWTA)

from .subject_screening_eligibility import SubjectScreeningEligibility
from .identifiers import ScreeningIdentifier


class SubjectScreeningManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, screening_identifier):
        return self.get(screening_identifier=screening_identifier)


class SubjectIdentifierModelMixin(NonUniqueSubjectIdentifierModelMixin,
                                  SearchSlugModelMixin, models.Model):

    def update_subject_identifier_on_save(self):
        """Overridden to not set the subject identifier on save.
        """
        if not self.subject_identifier:
            self.subject_identifier = self.subject_identifier_as_pk.hex
        elif re.match(UUID_PATTERN, self.subject_identifier):
            pass
        return self.subject_identifier

    def make_new_identifier(self):
        return self.subject_identifier_as_pk.hex

    class Meta:
        abstract = True


class SubjectScreening(SubjectIdentifierModelMixin):
    eligibility_cls = SubjectScreeningEligibility

    identifier_cls = ScreeningIdentifier

    age_in_years = models.IntegerField()
    gender = models.CharField(
        choices=GENDER,
        max_length=10)
    a_citizen = models.CharField(
        verbose_name='Are you a Botswana Citizen?',
        max_length=30,
        choices=YES_NO)
    not_a_citizen = models.CharField(
        verbose_name=('Are you married to to a Motswana?'
                      'Do you have a Marriage certificate?'),
        max_length=30,
        choices=YES_NO_MC)
    eligible = models.CharField(
        verbose_name='Are you a Minor?',
        max_length=30,
        choices=YES_NO_GP)
    literacy = models.CharField(
        verbose_name='Literate , Illiterate , Or Otherwise',
        max_length=30,
        choices=YES_NO_LW)
    '''Subject_Consent'''
    marital_status = models.CharField(
        verbose_name='Marital Status?',
        max_length=30,
        choices=MARITAL_STATUS)
    address = models.CharField(
        verbose_name='Who do you currently live with?',
        max_length=30,
        choices=ADDRESS)
    screening_identifier = models.CharField(
        verbose_name='Screening ID',
        max_length=50,
        blank=True,
        unique=True,
        editable=False)
    '''Educational_Background'''
    job_status = models.CharField(
        verbose_name='Are you currently working?',
        max_length=30,
        choices=YES_NO)
    job_details = models.CharField(
        verbose_name=('In your job, what type of work do you do?'),
        max_length=20,
        choices=JOB_DETAILS)
    job_description = models.CharField(
        verbose_name=('Describe the work that you do'
                      'or did in your most recent job.'
                      'If you have more than one profession,'
                      'choose the one you spend the most time doing.'),
        max_length=30,
        choices=JOB_DESCRIPTION)
    job_income = models.CharField(
        verbose_name=('In the past month, how much money did you earn?'),
        max_length=30,
        choices=JOB_INCOME)
    ''' Community_Engagement '''
    community_activity = models.CharField(
        verbose_name=('How active are you in community activities?'),
        max_length=30,
        choices=COMMUNITY_ACTIVITY)
    voting = models.CharField(
        verbose_name=('Did you vote in the last local government election?'),
        max_length=30,
        choices=YES_NO_NA_DWTA)
    neighborhood_problems = models.CharField(
        verbose_name=('What are the major problems in your neighborhood ?'),
        max_length=30,
        choices=NEIGHBORHOOD_PROBLEMS)
    neighborhood_problems_solved = models.CharField(
        verbose_name=('If there is a problem in this neighborhood,'
                      'do the adults work together in solving it?'),
        max_length=30,
        choices=YES_NO_DWTA)
    eligible = models.BooleanField(
        default=False,
        editable=False)
    reasons_ineligible = models.TextField(
        verbose_name='Reason not eligible',
        max_length=150,
        null=True,
        editable=False)

    consented = models.BooleanField(
        default=False,
        editable=False)

    def save(self, *args, **kwargs):
        eligibility_obj = self.eligibility_cls(model_obj=self, allow_none=True)
        self.eligible = eligibility_obj.eligible
        if not self.eligible:
            reasons_ineligible = [
                v for v in eligibility_obj.reasons_ineligible.values() if v]
            reasons_ineligible.sort()
            self.reasons_ineligible = ','.join(reasons_ineligible)
        else:
            self.reasons_ineligible = None
        if not self.id:
            self.screening_identifier = self.identifier_cls().identifier
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.screening_identifier, )
    natural_key.dependencies = ['sites.Site']

    def get_search_slug_fields(self):
        return ['screening_identifier', 'subject_identifier', 'reference']

    @property
    def estimated_dob(self):
        return get_utcnow().date() - relativedelta(years=self.age_in_years)
