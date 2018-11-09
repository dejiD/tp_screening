class GenderEvaluator:
    """Eligible if gender is valid
    """

    def __init__(self, gender=None):
        self.eligible = False
        self.reasons_eligible = None

        if gender == 'MALE':
            self.eligible = True
        elif gender == 'FEMALE':
            self.eligible = True

        else:
            self.eligible = False
