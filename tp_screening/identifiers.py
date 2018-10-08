'''
Created on 28 Sep 2018

@author: Deji
'''
from edc_identifier.simple_identifier import SimpleUniqueIdentifier
from tp_screening.choices import COUNTRY


class ScreeningIdentifier(SimpleUniqueIdentifier):

    random_string_length = 5
    identifier_type = 'screening_identifier'
    template = 'S{device_id}{random_string}'
    citizenship_evaluator = (COUNTRY, 'BOTSWANA'),
    citizenship_criteria = ('Married to a citizen'
                            'and has a marriage certificate')
