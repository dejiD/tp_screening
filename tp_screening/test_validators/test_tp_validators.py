from django.core.exceptions import ValidationError
from django.test import TestCase
from ..form_validators import TpFormValidator
from tp_screening.constants import YES, NO, NOT_APPLICABLE


class TestTpForm(TestCase):

    def test_age_is_18_valid(self):
        '''True if age is 18
        '''
        cleaned_data = {
            "age_in_years": 20,
        }
        form_validator = TpFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_age_is_not_18_invalid(self):
        '''Assert raises exception if age is less than 18
        '''
        cleaned_data = {
            "age_in_years": 17,
        }
        form_validator = TpFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('age_in_years', form_validator._errors)

    def test_age_is_invalid_gaurdian_not_present(self):
        '''Assert Raises exception if age is years is < 18, but guardian is not present.
        '''
        cleaned_data = {
            "age_in_years": 17,
            "guardian_present": NOT_APPLICABLE
        }
        form_validator = TpFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('age_in_years', form_validator._errors)

    def test_age_is_greater_than_18_valid_without_guardian(self):
        '''True if age is more than 18 and guardian is not present.
        '''
        cleaned_data = {
            "age_in_years": 20,
            "guardian_present": NOT_APPLICABLE
        }
        form_validator = TpFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_citizenship_valid_married_to_a_citizen(self):
        '''True if citizen is NO but married to a citizen and has proof are yes.
        '''
        cleaned_data = {
            "citizen_of_Botswana": NO,
            "married_to_a_citizen": YES,
            "proof_of_marriage": YES
        }
        form_validator = TpFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_citizenship_invalid_married_to_a_citizen_no(self):
        '''Assert raises exception if citizenship is no and married to citizen is no.
        '''
        cleaned_data = {
            "citizen_of_Botswana": NO,
            "married_to_a_citizen": NO,
            "proof_of_marriage": NO
        }
        form_validator = TpFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('citizen_of_Botswana', form_validator._errors)

    def test_literate_valid(self):
        '''True if literate.
        '''
        cleaned_data = {
            "literacy_status": YES,
            "literate_witness": NO
        }
        form_validator = TpFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_literate_invalid(self):
        '''Assert raises exception if literacy status is no and literacy witness is no.
        '''
        cleaned_data = {
            "literacy_status": NO,
            "literate_witness": NO
        }
        form_validator = TpFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('literacy_status', form_validator._errors)

    def test_literate_valid_no(self):
        '''True if literate.
        '''
        cleaned_data = {
            "literacy_status": NO,
            "literate_witness": YES
        }
        form_validator = TpFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
