from django.test import TestCase
from ..eligibility import CitizenshipEvaluator
from edc_constants.constants import (YES, NO)
from tp_screening.constants import NOT_APPLICABLE


class TestCitizenshipEvaluator(TestCase):

    def test_valid_citizenship(self):
        citizenship_evaluator = CitizenshipEvaluator(citizenship=YES)
        self.assertTrue(citizenship_evaluator.eligible)

    def test_not_a_citizen(self):
        citizenship_evaluator = CitizenshipEvaluator(citizenship=NO)
        self.assertFalse(citizenship_evaluator.eligible)

    def test_married_to_a_citizen(self):
        citizenship_evaluator = CitizenshipEvaluator(citizenship=NO,
                                                     married_to_a_citizen=YES,
                                                     proof_of_marriage=YES)
        self.assertTrue(citizenship_evaluator.eligible)

    def test_not_married_to_a_citizen(self):
        citizenship_evaluator = CitizenshipEvaluator(citizenship=NO,
                                                     married_to_a_citizen=NO,
                                                     proof_of_marriage=NO)
        self.assertFalse(citizenship_evaluator.eligible)

    def test_married_to_a_citizen_na(self):
        citizenship_evaluator = CitizenshipEvaluator(citizenship=NO,
                                                     married_to_a_citizen=NOT_APPLICABLE,
                                                     proof_of_marriage=NOT_APPLICABLE)
        self.assertFalse(citizenship_evaluator.eligible)

    def test_married_to_a_citizen_no(self):
        citizenship_evaluator = CitizenshipEvaluator(citizenship=NO,
                                                     married_to_a_citizen=NOT_APPLICABLE,
                                                     proof_of_marriage=YES)
        self.assertFalse(citizenship_evaluator.eligible)

    def test_married_to_a_citizen_invalid(self):
        citizenship_evaluator = CitizenshipEvaluator(citizenship=NO,
                                                     married_to_a_citizen=YES,
                                                     proof_of_marriage=NOT_APPLICABLE)
        self.assertFalse(citizenship_evaluator.eligible)

    def test_married_to_a_citizen_na_invalid(self):
        citizenship_evaluator = CitizenshipEvaluator(citizenship=NO,
                                                     married_to_a_citizen=YES,
                                                     proof_of_marriage=NO)
        self.assertFalse(citizenship_evaluator.eligible)
