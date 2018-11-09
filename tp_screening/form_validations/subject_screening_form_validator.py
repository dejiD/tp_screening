from edc_constants.constants import YES, NO, MALE, FEMALE
from edc_form_validators import FormValidator


class SubjectScreeningFormValidator(FormValidator):

    def clean(self):
        self.required_if_true(

        )
