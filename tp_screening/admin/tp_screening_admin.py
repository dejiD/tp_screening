from django.conf import settings
from django.contrib import admin


class TPScreeningAdmin(admin.ModelAdmin):

    post_url_on_delete_name = settings.DASHBOARD_URL_NAMES.get(
        'screening_dashboard_url')

    radio_fields = {
        'gender': admin.VERTICAL,
        'a_citizen': admin.VERTICAL,
        'not_a_citizen': admin.VERTICAL,
        'eligible': admin.VERTICAL,
        'literacy': admin.VERTICAL,
        'marital_status': admin.VERTICAL,
        'address': admin.VERTICAL,
        'job_status': admin.VERTICAL,
        'job_details': admin.VERTICAL,
        'job_description': admin.VERTICAL,
        'job_income': admin.VERTICAL,
        'community_activity': admin.VERTICAL,
        'voting': admin.VERTICAL,
        'neighborhood_problems': admin.VERTICAL,
        'neighborhood_problems_solved': admin.VERTICAL,
        }

    fieldsets = (
        (None, {
            'fields': (
                'gender',
                'a_citizen',
                'not_a_citizen',
                'eligible',
                'literacy',
                'marital_status',
                'address',
                'job_status',
                'job_details',
                'job_description',
                'job_income',
                'community_activity',
                'voting',
                'neighborhood_problems',
                'neighborhood_problems_solved',)
        }),

    admin.site.register(SubjectScreening,TPScreeningAdmin)