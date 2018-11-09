from edc_constants.constants import YES, NO
from tp_screening.constants import NOT_APPLICABLE


class CitizenshipEvaluator:

    def __init__(self, citizenship=None,
                 married_to_a_citizen=None, proof_of_marriage=None):

        self.eligible = False
        self.reasons_ineligible = None
        if citizenship == YES:
            self.eligible = True
        elif (citizenship == NO and married_to_a_citizen == YES
              and proof_of_marriage == YES):
            self.eligible = True
        elif (citizenship == YES and married_to_a_citizen == NOT_APPLICABLE
              and proof_of_marriage == NOT_APPLICABLE):
            self.eligible = True
        elif (citizenship == YES and married_to_a_citizen == NOT_APPLICABLE
              and proof_of_marriage == NOT_APPLICABLE):
            self.eligible = True
        else:
            self.eligible = False
