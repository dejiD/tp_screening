from .age_evaluator import AgeEvaluator
from .citizenship_evaluator import CitizenshipEvaluator
from .literacy_evaluator import LiteracyEvaluator


class EligibilityError(Exception):
    pass


class Eligibility:

    """Eligible if all criteria evaluate True.
    Any key in `additional_criteria` has value True if eligible.
    """
    age_evaluator = AgeEvaluator
    citizenship_evaluator = CitizenshipEvaluator
    literacy_evaluator = LiteracyEvaluator

    def __init__(self, age_in_years=None, minor=None, legal_witness=None,
                 married_to_a_citizen=None, proof_of_marriage=None,
                 literate_witness=None, citizen_of_Botswana=None,
                 literacy_status=None):

        self.criteria = dict()

        self.age_evaluator = self.age_evaluator(
            age_in_years, legal_witness, minor)

        self.literacy_evaluator = self.literacy_evaluator(
            literacy_status, literate_witness)

        self.citizenship_evaluator = self.citizenship_evaluator(
            citizen_of_Botswana, married_to_a_citizen, proof_of_marriage)

        self.criteria.update(
            age_in_years=self.age_evaluator.eligible)
        self.criteria.update(
            literacy_status=self.literacy_evaluator.eligible)
        self.criteria.update(
            citizen_of_Botswana=self.citizenship_evaluator.eligible)

        # eligible if all criteria are True
        self.eligible = all([v for v in self.criteria.values()])
        if self.eligible:
            self.reasons_ineligible = None
        else:
            self.reasons_ineligible = {
                k: v for k, v in self.criteria.items() if not v}
            if not self.age_evaluator.eligible:
                self.reasons_ineligible.update(
                    age_in_years=self.age_evaluator.reasons_ineligible)
            if not self.literacy_evaluator.eligible:
                self.reasons_ineligible.update(
                    literacy_status=self.literacy_evaluator.reasons_ineligible)
            if not self.citizenship_evaluator.eligible:
                self.reasons_ineligible.update(
                    citizen_of_Botswana=self.citizenship_evaluator.reasons_ineligible)

    def __str__(self):
        return self.eligible
