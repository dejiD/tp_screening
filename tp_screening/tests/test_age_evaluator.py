from django.test import TestCase

from ..tp_reportables import age_evaluator


class TestAgeEvaluator(TestCase):

    def test_eligibility_valid_age_in_years(self):
        self.assertTrue(age_evaluator.eligible(19))

    def test_eligibility_valid_age(self):
        self.assertTrue(age_evaluator.eligible(18))

    def test_eligibility_invalid_age_in_years(self):
        self.assertFalse(age_evaluator.eligible(17))

    def test_eligibility_invalid_age_in_years_reasons_ineligible(self):
        age_evaluator.eligible(15)
        self.assertIn('age<18.', age_evaluator.reasons_ineligible)
        age_evaluator.eligible(17)
        self.assertIn('age<18.', age_evaluator.reasons_ineligible)
        age_evaluator.eligible(18)
        self.assertIsNone(age_evaluator.reasons_ineligible)

    def test_eligibility_invalid_age_with_legal_witness(self):
        age_evaluator.eligible(14)
        self.assertFalse(age_evaluator.eligible(14))

    def test_eligibility_invalid_age_without_legal_witnness(self):
        age_evaluator.eligible(14)
        self.assertFalse(age_evaluator.eligible(14))
