'''
Created on 28 Sep 2018

@author: Deji
'''
from .gender_evaluator import GenderEvaluator
from .tp_reportables import age_evaluator
from .citizenship_evaluator import CitizenshipEvaluator
from .literacy_evaluator import LiteracyEvaluator


class EligibilityError(Exception):
    pass


class Eligibility:

    """Eligible if all criteria evaluate True.
    Any key in `additional_criteria` has value True if eligible.
    """
    gender_evaluator_cls = GenderEvaluator
    age_evaluator = age_evaluator
    citizenship_evaluator = CitizenshipEvaluator
    literacy_evaluator = LiteracyEvaluator

    def __init__(self, **additional_criteria):
        self.criteria = dict(**additional_criteria)
        print (self.criteria)

        if len(self.criteria) == 0:
            raise EligibilityError('No criteria provided.')
            self.eligible = True

    def __str__(self):
        return self.eligible
