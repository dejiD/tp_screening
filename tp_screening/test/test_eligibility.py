
from django.test import TestCase
from ..eligibility import Eligibility, EligibilityError
from tp_screening.tp_reportables import age_evaluator


class TestEligibility(TestCase):

    def setUp(self):
        self.evaluator_criteria = dict(
            age=18,
            gender='FEMALE, MALE',
            country='BOTSWANA',
            married='MARRIAGE CERTIFICATE',
            literacy='literate',
            )

    def test_eligibility_without_criteria(self):
        self.assertRaises(EligibilityError, Eligibility)

    def test_eligibility_with_criteria(self):
        self.assertRaises(EligibilityError)

    def test_eligibility_ok(self):
        self.assertTrue(age_evaluator.eligible(18))

    def test_eligibility_not_ok_by_age_only(self):
        self.evaluator_criteria.update(age=17)
        self.assertTrue(age_evaluator.eligible)
        self.assertTrue(age_evaluator.eligible, {'age': 'age<18.'})

    def test_eligibility_ok_by_age_only(self):
        self.evaluator_criteria.update(age=19)
        self.assertTrue(age_evaluator.eligible)
        self.assertTrue(age_evaluator.eligible, {'age': 'age>18.'})
