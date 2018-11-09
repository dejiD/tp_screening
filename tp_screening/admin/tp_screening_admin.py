from django.conf import settings
from django.contrib import admin
from ..forms import SubjectScreeningForm
from ..models import SubjectScreening
from ..admin_site import tp_screening_admin
from .model_admin_mixin import ModelAdminMixin


@admin.register(SubjectScreening, site=tp_screening_admin)
class TPScreeningAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SubjectScreeningForm

    post_url_on_delete_name = settings.DASHBOARD_URL_NAMES.get(
        'screening_dashboard_url')

    radio_fields = {
        'age_in_years': admin.VERTICAL,
        'gender': admin.VERTICAL,
        'minor': admin.VERTICAL,
        'gaurdian_present': admin.VERTICAL,
        'citizen_of_Botswana': admin.VERTICAL,
        'marital_status': admin.VERTICAL,
        'married_to_a_citizen': admin.VERTICAL,
        'proof_of_marriage': admin.VERTICAL,
        'job_status': admin.VERTICAL,
        'job_details': admin.VERTICAL,
        'job_income': admin.VERTICAL,
        'job_description': admin.VERTICAL,
        'literacy_status': admin.VERTICAL,
        'literate_witness': admin.VERTICAL,
    }

    fieldsets = (
        (None, {
            'fields': (
                'age_in_years',
                'gender',
                'minor',
                'gaurdian_present',
                'citizen_of_Botswana',
                'marital_status',
                'married_to_a_citizen',
                'proof_of_marriage',
                'job_status',
                'job_details',
                'job_income',
                'job_description',
                'literacy_status',
                'literate_witness')
        })),
