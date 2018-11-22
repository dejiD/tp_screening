from edc_form_validators import FormValidator
from django.core.exceptions import ValidationError
from tp_screening.constants import NO, NOT_APPLICABLE


class TpFormValidator(FormValidator):

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('age_in_years'):
            if cleaned_data.get('age_in_years') < 18:
                msg = {'age_in_years': 'Your age is less than 18, you need a guardian.'
                       }
                self._errors.update(msg)
                raise ValidationError(msg)

        cleaned_data = self.cleaned_data
        if cleaned_data.get('age_in_years'):
            if cleaned_data.get('age_in_years') < 18 and (
                    cleaned_data.get('guardian_present') == NO or NOT_APPLICABLE):
                msg = {'age_in_years': 'Your age is less than 18, you need a guardian.'
                       }
                self._errors.update(msg)
                raise ValidationError(msg)

        cleaned_data = self.cleaned_data
        if cleaned_data.get('citizen_of_Botswana'):
            if cleaned_data.get('citizen_of_Botswana') == NO and (
                cleaned_data.get('married_to_a_citizen') == NO) or (
                    cleaned_data.get('married_to_a_citizen') == NOT_APPLICABLE) or (
                    cleaned_data.get('proof_of_marriage') == NO) or (
                        cleaned_data.get('proof_of_marriage') == NOT_APPLICABLE):
                msg = {'citizen_of_Botswana': 'You need to be a citizen or '
                       'married to a citizen with proof of marriage'
                       }
                self._errors.update(msg)
                raise ValidationError(msg)

        cleaned_data = self.cleaned_data
        if cleaned_data.get('literacy_status'):
            if cleaned_data.get('literacy_status') == NO and (
                    cleaned_data.get('literate_witness') == NO) or (
                        cleaned_data.get('literate_witness') == NOT_APPLICABLE):
                msg = {'literacy_status': 'You need to be literate or have a '
                       'literate witness'
                       }
                self._errors.update(msg)
                raise ValidationError(msg)
