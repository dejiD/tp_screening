
from .eligibility import Eligibility


class SubjectScreeningEligibility:

    eligibility_cls = Eligibility

    def __init__(self, model_obj=None):
        eligibility_obj = self.eligibility_cls(
            age_in_years=model_obj.age_in_years,
            literacy_status=model_obj.literacy_status,
            citizen_of_Botswana=model_obj.citizen_of_Botswana
        )
        self.eligible = eligibility_obj.eligible
        self.reasons_ineligible = eligibility_obj.reasons_ineligible
