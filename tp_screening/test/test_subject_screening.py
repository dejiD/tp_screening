'''
Created on 04 Oct 2018

@author: Deji
'''
from django.test import TestCase, tag
from edc_base.tests import SiteTestCaseMixin
from edc_constants.constants import FEMALE, MALE
from model_mommy import mommy


class TestSubjectScreening(SiteTestCaseMixin, TestCase):

    @tag('1')
    def test_eligible_with_default_recipe_criteria(self):
        subject_screening = mommy.make_recipe(
            'tp_screening.subjectscreening')
        self.assertTrue(subject_screening.eligible)
        self.assertTrue(subject_screening.gender, MALE, FEMALE)

    def test_subject_invalid_age(self):
        subject_screening = mommy.prepare_recipe(
            'tp_screening.subjectscreening', age_in_years=16)
        self.assertFalse(subject_screening.eligible)

    def test_subject_age_minor_invalid_reason(self):
        subject_screening = mommy.make_recipe(
            'tp_screening.subjectscreening', age_in_years=17)
        self.assertFalse(subject_screening.eligible)
        self.assertIn(
            subject_screening.reasons_ineligible, 'age<18.')

    def test_subject_age_valid_no_reason(self):
        subject_screening = mommy.make_recipe(
            'tp_screening.subjectscreening', age_in_years=18)
        self.assertTrue(subject_screening.eligible)
        self.assertEqual(subject_screening.reasons_ineligible, None)
