'''
Created on 03 Oct 2018

@author: Deji
'''
# from django.contrib.sites.models import Site
from edc_constants.constants import YES, MALE
from faker import Faker
from model_mommy.recipe import Recipe

from .models import SubjectScreening


fake = Faker()

subject_screening = Recipe(
    SubjectScreening,
    a_citizen=YES,
    not_a_citizen=YES,
    marital_status=YES,
    gender=MALE,
    age_in_years=18,
    literacy=YES)
