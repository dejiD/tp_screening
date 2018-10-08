'''
Created on 04 Oct 2018

@author: Deji
'''
from edc_constants.constants import YES, NO


class LiteracyEvaluator:
    def __init__(self, literate=True, iliterate=True):
        self.eligible = False
        self.reasons_ineligible = None

        if literate == YES:
            self.eligible = True
        elif iliterate == NO:
            self.eligible = False

        if iliterate == YES:
            self.reasons_ineligible = ('Literate_witness')
