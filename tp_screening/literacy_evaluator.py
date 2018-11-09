from edc_constants.constants import YES, NO, NOT_APPLICABLE


class LiteracyEvaluator:
    def __init__(self, literacy=True, literate_witness=None):
        self.eligible = False
        self.reasons_ineligible = None

        self.eligible = False
        self.reasons_ineligible = None
        if literacy == YES:
            self.eligible = True
        elif (literacy == NO and literate_witness == YES):
            self.eligible = True
        elif (literacy == YES and literate_witness == NOT_APPLICABLE):
            self.eligible = True
        else:
            self.eligible = False
