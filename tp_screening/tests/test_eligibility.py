
from django.test import TestCase
from ..eligibility import Eligibility, EligibilityError
from ..tp_reportables import age_evaluator
from edc_constants.constants import YES, NO, NOT_APPLICABLE
from tp_screening.literacy_evaluator import LiteracyEvaluator


class TestEligibility(TestCase):

    def setUp(self):
        self.evaluator_criteria = dict(
            age_in_years=18,
            citizenship=YES,
            citizen_of_Botswana=YES,
            married_to_a_citizen=YES, proof_of_marriage=YES,
            literacy=YES,
            literate_witness=YES
        )

    def test_eligibility_without_criteria(self):
        obj = Eligibility(self.evaluator_criteria)
        self.assertFalse(obj.eligible)
        self.assertRaises(EligibilityError)

    def test_eligibility_with_criteria(self):
        obj = Eligibility(self.evaluator_criteria)
        self.assertFalse(obj.eligible)
        self.assertRaises(EligibilityError)

    def test_eligibility_ok(self):
        obj = Eligibility(self.evaluator_criteria)
        self.assertFalse(obj.eligible)
        self.assertTrue(age_evaluator.eligible(18))

    def test_eligibility_less_than_18(self):
        obj = Eligibility(self.evaluator_criteria)
        self.assertFalse(obj.eligible)
        self.assertFalse(age_evaluator.eligible(16))

    def test_eligibility_not_ok_by_age(self):
        obj = Eligibility(self.evaluator_criteria)
        self.assertFalse(obj.eligible)
        self.evaluator_criteria.update(age=17)
        self.assertTrue(age_evaluator.eligible)
        self.assertTrue(age_evaluator.eligible, {'age': 'age<18.'})

    def test_eligibility_ok_by_age_only(self):
        obj = Eligibility(self.evaluator_criteria)
        self.assertFalse(obj.eligible)
        self.evaluator_criteria.update(age=19)
        self.assertTrue(age_evaluator.eligible)
        self.assertTrue(age_evaluator.eligible, {'age': 'age>18.'})

    def test_eligibility_citizenship_yes(self):
        obj = Eligibility(citizen_of_Botswana=YES)
        self.assertFalse(obj.eligible)

    def test_eligibility_citizenship_no(self):
        obj = Eligibility(citizen_of_Botswana=NO)
        self.assertFalse(obj.eligible)

    def test_eligibility_married_to_a_citizen_na(self):
        obj = Eligibility(citizen_of_Botswana=NO, married_to_a_citizen=NOT_APPLICABLE,
                          proof_of_marriage=NOT_APPLICABLE)
        self.assertFalse(obj.eligible)

    def test_eligibility_married_to_a_citizen_no(self):
        obj = Eligibility(citizen_of_Botswana=NO, married_to_a_citizen=NOT_APPLICABLE,
                          proof_of_marriage=YES)
        self.assertFalse(obj.eligible)

    def test_eligibility_married_to_a_citizen_invalid(self):
        obj = Eligibility(citizen_of_Botswana=NO, married_to_a_citizen=YES,
                          proof_of_marriage=NOT_APPLICABLE)
        self.assertFalse(obj.eligible)

    def test_eligibility_married_to_a_citizen_na_invalid(self):
        obj = Eligibility(citizen_of_Botswana=NO,
                          married_to_a_citizen=YES,
                          proof_of_marriage=NO)
        self.assertFalse(obj.eligible)

    def test_eligibility_literate_yes(self):
        obj = Eligibility(self.evaluator_criteria)
        self.assertFalse(obj.eligible)
        literacy_evaluator = LiteracyEvaluator(literacy=YES)
        self.assertTrue(literacy_evaluator.eligible)

    def test_eligibility_literate_no(self):
        obj = Eligibility(self.evaluator_criteria)
        self.assertFalse(obj.eligible)
        literacy_evaluator = LiteracyEvaluator(literacy=NO)
        self.assertFalse(literacy_evaluator.eligible)

    def test_eligibility_literate_na(self):
        obj = Eligibility(self.evaluator_criteria)
        self.assertFalse(obj.eligible)
        literacy_evaluator = LiteracyEvaluator(literacy=NO,
                                               literate_witness=NOT_APPLICABLE)
        self.assertFalse(literacy_evaluator.eligible)

    def test_eligibility_literate_na_yes(self):
        obj = Eligibility(self.evaluator_criteria)
        self.assertFalse(obj.eligible)
        literacy_evaluator = LiteracyEvaluator(literacy=YES,
                                               literate_witness=NOT_APPLICABLE)
        self.assertTrue(literacy_evaluator.eligible)

    def test_eligibility_literate_no_yes(self):
        obj = Eligibility(self.evaluator_criteria)
        self.assertFalse(obj.eligible)
        literacy_evaluator = LiteracyEvaluator(literacy=NO,
                                               literate_witness=YES)
        self.assertTrue(literacy_evaluator.eligible)
