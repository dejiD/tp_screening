'''
Created on 28 Sep 2018

@author: Deji
'''
from edc_identifier.simple_identifier import SimpleUniqueIdentifier


class ScreeningIdentifier(SimpleUniqueIdentifier):

    random_string_length = 5
    identifier_type = 'screening_identifier'
    template = 'S{device_id}{random_string}'
