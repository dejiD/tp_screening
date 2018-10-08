'''
Created on 04 Oct 2018

@author: Deji
'''
from django.test import TestCase
from ..eligibility import CitizenshipEvaluator
from ..choices import MARRIED


class TestCitizenshipEvaluator(TestCase):

    def test_eligibility_valid_citizenship(self):
        citizenship_evaluator = CitizenshipEvaluator(COUNTRY='BOTSWANA')
        self.assertFalse(citizenship_evaluator.eligible)

    def test_eligibilty_not_a_citizen(self):
        citizenship_evaluator = CitizenshipEvaluator(COUNTRY='BOTSWANA')
        self.assertFalse(citizenship_evaluator.eligible)

    def test_eligibility_married_to_a_citizen(self):
        citizenship_evaluator = CitizenshipEvaluator(MARRIED=MARRIED)
        self.assertFalse(citizenship_evaluator.eligible)

    def test_eligibility_gender_not_married_to_a_citizen(self):
        citizenship_evaluator = CitizenshipEvaluator(MARRIED=MARRIED)
        self.assertFalse(citizenship_evaluator.eligible)
