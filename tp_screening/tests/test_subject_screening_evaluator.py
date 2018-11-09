from edc_base.tests.site_test_case_mixin import SiteTestCaseMixin
from django.test import TestCase
from model_mommy import mommy
from edc_constants.constants import YES, NO


class TestSubjectScreening(SiteTestCaseMixin, TestCase):
    def __init__(self, *kwargs):
        self.reasons_eligible = None
        super().__init__(*kwargs)

    def test_eligibility_with_default_recipe_creteria(self):
        subject_screening = mommy.make_recipe('tp_screening.subject_screening')
        self.assertTrue(subject_screening.eligible)

    def test_eligibility_with_default_recipe(self):
        subject_screening = mommy.make_recipe('tp_screening.subject_screening')
        self.assertTrue(subject_screening.gender)

    def test_eligibility_invalid_age(self):
        subject_screening = mommy.make_recipe('tp_screening.subject_screening',
                                              age_in_years=17)
        self.assertFalse(subject_screening.eligible)

    def test_eligibility_valid_age(self):
        subject_screening = mommy.make_recipe('tp_screening.subject_screening',
                                              age_in_years=18)
        self.assertTrue(subject_screening.eligible)

    def test_eligibility_valid_citizen(self):
        subject_screening = mommy.make_recipe('tp_screening.subject_screening',
                                              citizen_of_Botswana=YES)
        self.assertTrue(subject_screening.eligible)

    def test_eligibility_invalid_citizen_no(self):
        subject_screening = mommy.make_recipe('tp_screening.subject_screening',
                                              citizen_of_Botswana=NO)
        self.assertFalse(subject_screening.eligible)

    def test_eligibility_valid_literate(self):
        subject_screening = mommy.make_recipe('tp_screening.subject_screening',
                                              literacy_status=YES)
        self.assertTrue(subject_screening.eligible)

    def test_eligibility_invalid_literate(self):
        subject_screening = mommy.make_recipe('tp_screening.subject_screening',
                                              literacy_status=NO)
        self.assertFalse(subject_screening.eligible)

    def test_eligibility_minor(self):
        subject_screening = mommy.make_recipe('tp_screening.subject_screening',
                                              minor=NO)
        self.assertTrue(subject_screening.eligible)

    def test_eligibility_minor_yes(self):
        subject_screening = mommy.make_recipe('tp_screening.subject_screening',
                                              minor=YES)
        self.assertFalse(subject_screening.eligible)

    def test_eligibility_literate_witness_yes(self):
        subject_screening = mommy.make_recipe('tp_screening.subject_screening',
                                              literate_witness=YES)
        self.assertTrue(subject_screening.eligible)

    def test_eligibility_literate_witness_no(self):
        subject_screening = mommy.make_recipe('tp_screening.subject_screening',
                                              literate_witness=NO)
        self.assertFalse(subject_screening.eligible)
