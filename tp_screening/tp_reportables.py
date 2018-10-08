from dateutil.relativedelta import relativedelta
from edc_base.utils import get_utcnow
from edc_reportable import ValueBoundryError
from edc_reportable import AgeEvaluator
from django.utils.timezone import localtime

from tp_screening.choices import COUNTRY
from tp_screening.citizenship_evaluator import CitizenshipEvaluator


class MyAgeEvaluator(AgeEvaluator):

    def __init__(self, **kwargs):
        self.reasons_ineligible = None
        super().__init__(**kwargs)

    def eligible(self, age=None):
        self.reasons_ineligible = None
        eligible = False
        if age:
            try:
                self.in_bounds_or_raise(age=age)
            except ValueBoundryError:
                self.reasons_ineligible = 'age<18.'
            else:
                eligible = True
        return eligible

    def in_bounds_or_raise(self, age=None):
        self.reasons_ineligible = None
        dob = localtime(get_utcnow() - relativedelta(years=age)).date()
        age_units = 'years'
        report_datetime = localtime(get_utcnow())
        return super().in_bounds_or_raise(
            dob=dob, report_datetime=report_datetime, age_units=age_units)


age_evaluator = MyAgeEvaluator(
    age_higher_inclusive=True,
    age_lower=18,
    age_lower_inclusive=True)

citizenship_evaluator = CitizenshipEvaluator(
    COUNTRY=(COUNTRY, 'BOTSWANA'),
    citizenship_criteria=('Married to a citizen'
                          'and has a marriage certificate'))
