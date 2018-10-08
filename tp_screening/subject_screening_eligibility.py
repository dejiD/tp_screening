
from .eligibility import Eligibility


class SubjectScreeningEligibility:

    eligibility_cls = Eligibility

    def __init__(self, model_obj=None, allow_none=None):
        eligibility_obj = self.eligibility_cls(
            allow_none=allow_none,
            age=model_obj.age_in_years,
            gender=model_obj.gender,
            subject_screening=model_obj
        )
        self.eligible = eligibility_obj.eligible
        self.reasons_ineligible = eligibility_obj.reasons_ineligible
