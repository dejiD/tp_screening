import re
from dateutil.relativedelta import relativedelta
from edc_constants.constants import UUID_PATTERN
from django.db import models
from edc_search.model_mixins import SearchSlugManager, SearchSlugModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_base.utils import get_utcnow
from ..subject_screening_eligibility import SubjectScreeningEligibility
from ..identifiers import ScreeningIdentifier
from tp_screening.choices.age_choices import GAURDIAN_PRESENT,\
    MINOR
from tp_screening.choices.citizen_choices import CITIZEN_OF_BOTSWANA,\
    MARRIED_TO_A_CITIZEN, PROOF_OF_MARRIAGE
from tp_screening.choices.married_choices import MARITAL_STATUS
from tp_screening.choices.gender_choices import GENDER
from tp_screening.choices.literacy_choices import LITERACY_STATUS,\
    LITERATE_WITNESS
from tp_screening.choices.job_choices import JOB_DESCRIPTION, JOB_DETAILS, JOB_INCOME,\
    JOB_STATUS
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from uuid import uuid4
from edc_base.model_managers import HistoricalRecords
from edc_base.sites import CurrentSiteManager


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


class SubjectScreening(SubjectIdentifierModelMixin, SiteModelMixin, BaseUuidModel):
    eligibility_cls = SubjectScreeningEligibility

    identifier_cls = ScreeningIdentifier

    reference = models.UUIDField(
        verbose_name='Reference',
        unique=True,
        default=uuid4,
        editable=False)

    screening_identifier = models.CharField(
        verbose_name='Screening ID',
        max_length=50,
        blank=True,
        unique=True,
        editable=False)

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

    age_in_years = models.IntegerField(
        verbose_name=("1. How old are you?"),
        help_text="",
    )

    gender = models.CharField(
        verbose_name=("2. Select your Gender"),
        max_length=15,
        choices=GENDER,
        help_text="",
    )

    minor = models.CharField(
        verbose_name=("3.Are you in the minor category?"),
        max_length=35,
        choices=MINOR,
        help_text="",
    )

    gaurdian_present = models.CharField(
        verbose_name=("4. Do you have a gaurdian present?"),
        max_length=35,
        choices=GAURDIAN_PRESENT,
        help_text="",
    )

    citizen_of_Botswana = models.CharField(
        verbose_name=("5. Are you a citizen of Botswana?"),
        max_length=15,
        choices=CITIZEN_OF_BOTSWANA,
        help_text="",
    )

    marital_status = models.CharField(
        verbose_name=("6. Are you married?"),
        max_length=15,
        choices=MARITAL_STATUS,
        help_text="",
    )

    married_to_a_citizen = models.CharField(
        verbose_name=("7. Are you married to a Motswana?"),
        max_length=35,
        choices=MARRIED_TO_A_CITIZEN,
        help_text="",
    )

    proof_of_marriage = models.CharField(
        verbose_name=("8. Do you have a proof of marriage?"),
        max_length=35,
        choices=PROOF_OF_MARRIAGE,
        help_text="",
    )

    literacy_status = models.CharField(
        verbose_name=("9. Are you Literate?"),
        max_length=15,
        choices=LITERACY_STATUS,
        help_text="",
    )

    literate_witness = models.CharField(
        verbose_name=("10. Do you have a Literate witness?"),
        max_length=35,
        choices=LITERATE_WITNESS,
        help_text="",
    )

    job_status = models.CharField(
        verbose_name=("11. Are you currently working?"),
        max_length=35,
        choices=JOB_STATUS,
        help_text="",
    )

    job_details = models.CharField(
        verbose_name=("12. In your main job what type of work do you do?"),
        max_length=35,
        choices=JOB_DETAILS,
        help_text="",
    )

    job_income = models.CharField(
        verbose_name=("13. In the past month, how much money did you earn"
                      "from work you did or received in payment?"),
        max_length=70,
        choices=JOB_INCOME,
        help_text="",
    )

    job_description = models.CharField(
        verbose_name=("14. Describe the work that you do or did in your most recent job."
                      "If you have more than one profession,"
                      "choose the one you spend the most time doing"),
        max_length=70,
        choices=JOB_DESCRIPTION,
        help_text="",
    )

    on_site = CurrentSiteManager()

    objects = SubjectScreeningManager()

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.screening_identifier} {self.gender} {self.age_in_years}'

    def save(self, *args, **kwargs):
        eligibility_obj = self.eligibility_cls(model_obj=self)
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
