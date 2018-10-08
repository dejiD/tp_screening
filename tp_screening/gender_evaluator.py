'''
Created on 28 Sep 2018

@author: Deji
'''
from edc_constants.constants import MALE, FEMALE
from tp_screening.choices import GENDER


class GenderEvaluator:
    """Eligible if gender is valid
    """

    def __init__(self, gender=None, **kwargs):
        self.eligible = False
        self.reasons_eligible = None

        if gender == MALE:
            self.eligible = True
        elif gender == FEMALE:
            self.eligible = True

        if gender not in [GENDER]:
            self.reasons_eligible = 'invalid'
