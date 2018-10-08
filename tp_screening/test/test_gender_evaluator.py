from django.test import TestCase
from edc_constants.constants import FEMALE, MALE

from ..eligibility import GenderEvaluator
from edc_constants.choices import GENDER_UNDETERMINED


class TestGenderEvaluator(TestCase):

    def test_eligibility_gender_female(self):
        gender_evaluator = GenderEvaluator(gender=FEMALE)
        self.assertTrue(gender_evaluator.eligible)

    def test_eligibilty_gender_male(self):
        gender_evaluator = GenderEvaluator(gender=MALE)
        self.assertTrue(gender_evaluator.eligible)

    def test_eligibility_gender_not_female(self):
        gender_evaluator = GenderEvaluator(gender=FEMALE)
        self.assertTrue(gender_evaluator.eligible)

    def test_eligibility_gender_not_male(self):
        gender_evaluator = GenderEvaluator(gender=MALE)
        self.assertTrue(gender_evaluator.eligible)

    def test_eligibility_gender_unsure(self):
        gender_evaluator = GenderEvaluator(gender=GENDER_UNDETERMINED)
        self.assertFalse(gender_evaluator.eligible)

    def test_eligibility_gender_undetermined(self):
        gender_evaluator = GenderEvaluator(gender=GENDER_UNDETERMINED)
        self.assertFalse(gender_evaluator.eligible)
