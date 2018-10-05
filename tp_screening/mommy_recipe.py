'''
Created on 03 Oct 2018

@author: Deji
'''
# from django.contrib.sites.models import Site
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, MALE
from faker import Faker
from model_mommy.recipe import Recipe

from .models import Subject_Screening

fake = Faker()

subjectscreening = Recipe(
    Subject_Screening,
    a_citizen=YES,
    married_to_a_citizen=YES,
    report_datetime=get_utcnow(),
    gender=MALE,
    age_in_years=18,
    literate=YES)
