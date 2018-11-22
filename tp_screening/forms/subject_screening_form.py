from ..form_validators import TpFormValidator
from django import forms
from edc_form_validators import FormValidatorMixin

from ..models.subject_screening import SubjectScreening


class SubjectScreeningForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = TpFormValidator

    class Meta:
        model = SubjectScreening
        fields = '__all__'
