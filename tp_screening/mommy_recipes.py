# from django.contrib.sites.models import Site
from edc_constants.constants import YES
from faker import Faker
from model_mommy.recipe import Recipe

from tp_screening.models.subject_screening import SubjectScreening


fake = Faker()

subject_screening = Recipe(
    SubjectScreening,
    citizen_of_Botswana=YES,
    married_to_a_citizen=YES,
    proof_of_marriage=YES,
    literacy_status=YES,
    literate_witness=YES,
    age_in_years=18,
    minor=YES,
    gaurdian_present=YES,
)
