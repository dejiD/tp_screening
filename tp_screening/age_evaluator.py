from edc_constants.constants import YES


class AgeEvaluator:

    def __init__(self, age_in_years=None, gaurdian_present=None, minor=None):

        self.eligible = False
        self.reasons_ineligible = None
        if age_in_years == 18:
            self.eligible = True
        elif age_in_years == minor and gaurdian_present == YES:
            self.eligible = True
        else:
            self.eligible = False
