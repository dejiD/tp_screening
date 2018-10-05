'''
Created on 28 Sep 2018

@author: Deji
'''
from .choices import (COUNTRY, MARRIED)


class CitizenshipEvaluator:

    def __init__(self, **kwargs):

        self.eligible = False
        self.reasons_ineligible = None
        if COUNTRY == 'BOTSWANA':
            self.eligible = True
        else:
            self.eligible = False
        if MARRIED == 'Married to a Motswana' and 'Has A Marriage Certificate':
            self.eligible = True
        else:
            self.eligible = False

    def __str__(self, **kwargs):
        self.eligible = False
        self.reasons_ineligible = None
