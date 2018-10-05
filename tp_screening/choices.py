from django.utils.translation import ugettext_lazy as _

from .constants import (
    DWTA, FEMALE, MALE, ALONE, OTHER, BOTSWANA,
    PARTNER_SPOUSE, NO_ANSWER, NONE,
    VERY_ACTIVE, SOMEWHAT_ACTIVE, NOT_ACTIVE_AT_ALL,
    FARMER, FARM_WORKER, DOMESTIC_WORKER,
    PRIVATE_WORKER, FISHING, MINING, TOURISM,
    SME, INFORMAL_SELLING, COMMERCIAL_SEX_WORKER, TRANSPORT,
    FACTORY, GAURD, POLICE_SOLDIER, CLERK, GOVERNMENT_WORKER,
    TEACHER, HEALTHCARE_WORKER, OTHER_PROFESSIONAL,
    SINGLE, MARRIED, DIVORCED, WIDOWED, HIV_AIDS, Schools,
    Sewer, Unemployment, Roads, Water, Other_specify, House, Malaria,
    NO, NOT_APPLICABLE, YES, Occassional_CasualEmployment,
    Seasonal_Employment, Formal_Wage_Employment, Self_Employed_Agriculture,
    Self_employed_Making_Money, Level_one, Level_two, Level_three, Level_four,
    Level_five, Level_six, Literate_Witness, GAURDIAN_PRESENT)

BLANK_CHOICE_DASH = [('', '---------')]

""" Try to keep these in alphabetical order
"""

ADDRESS = (
    (ALONE, _('Alone')),
    (PARTNER_SPOUSE, _('Partner/Spouse')),
    (OTHER, _('Other')),
    (NO_ANSWER, _('No Answer')),
)

COUNTRY = (
    (BOTSWANA, _('BOTSWANA')),
)

COMMUNITY_ACTIVITY = (
    (VERY_ACTIVE, _('VERY ACTIVE')),
    (SOMEWHAT_ACTIVE, _('SOMEWHAT ACTIVE')),
    (NOT_ACTIVE_AT_ALL, _('NOT ACTIVE AT ALL')),
    (DWTA, _('DO NOT WANT TO ANSWER')),
)

GENDER = (
    (MALE, _('Male')),
    (FEMALE, _('Female')),
    ('U', _('Undetermined')),
)

JOB_DESCRIPTION = (
    (FARMER, 'Farmer (own land)'),
    (FARM_WORKER, 'Farm work on employers land'),
    (DOMESTIC_WORKER, 'Domestic worker'),
    (PRIVATE_WORKER, 'Work in bar/ hotel/ guest house/ entertainment venue'),
    (FISHING, 'Fishing'),
    (MINING, 'Mining'),
    (TOURISM, 'Tourism/game parks'),
    (SME, 'Working in shop / small business'),
    (INFORMAL_SELLING, 'Informal selling'),
    (COMMERCIAL_SEX_WORKER, 'Commercial sex work'),
    (TRANSPORT, 'Transport (trucker/ taxi driver)'),
    (FACTORY, 'Factory worker'),
    (GAURD, 'Guard (security company)'),
    (POLICE_SOLDIER, 'Police/Soldier'),
    (CLERK, 'Clerical and office work'),
    (GOVERNMENT_WORKER, 'Government worker'),
    (TEACHER, 'Teacher'),
    (HEALTHCARE_WORKER, 'Health care worker'),
    (OTHER_PROFESSIONAL, 'Other professional'),
    (DWTA, 'Do not want to answer'),
    (OTHER, 'Other'),
)

JOB_INCOME = (
    (NONE, 'None'),
    (Level_one, '1-199 pula'),
    (Level_two, '200-499 pula'),
    (Level_three, '500-999 pula'),
    (Level_four, '1000-4999 pula'),
    (Level_five, '5000-10,000 pula'),
    (Level_six, 'More than 10,000 pula'),
    (DWTA, 'Do not want to answer'),
)

JOB_DETAILS = (
    (Occassional_CasualEmployment, _('Occassional_CasualEmployment(piece_job)')),
    (Seasonal_Employment, 'Seasonal_Employment'),
    (Formal_Wage_Employment, 'Formal_Wage-Employment(full-time)'),
    (Formal_Wage_Employment, 'FormalWageEmployment(part-time)'),
    (Self_Employed_Agriculture, 'Self-Employed_Agriculture'),
    (Self_employed_Making_Money, 'Self-employed-Making-Money(full time)'),
    (Self_employed_Making_Money, 'Self-Employed-Making-Money(part time)'),
    (DWTA, 'Do not want to answer'),
    (OTHER, 'Other'),
)

MARITAL_STATUS = (
    (SINGLE, 'Single'),
    (MARRIED, 'Married'),
    (DIVORCED, 'Divorced'),
    (WIDOWED, 'Widowed'),
)

NEIGHBORHOOD_PROBLEMS = (
    (HIV_AIDS, 'HIV/AIDS'),
    (Schools, 'Schools'),
    (Sewer, 'Sewer'),
    (Unemployment, 'Unemployment'),
    (Roads, 'Roads'),
    (Water, 'Water'),
    (Other_specify, 'Other, specify'),
    (House, 'House'),
    (Malaria, 'Malaria'),
)

YES_NO_LW = (
    (YES, _(YES)),
    (NO, _(NO)),
    (Literate_Witness, 'Literate Witness'),
)

YES_NO_MC = (
    (YES, _(YES)),
    (NO, _(NO)),
    (MARRIED, 'Marriage Certificate'),
)

YES_NO_GP = (
    (YES, _(YES)),
    (NO, _(NO)),
    (GAURDIAN_PRESENT, 'GAURDIAN PRESENT'),
)

YES_NO = (
    (YES, _(YES)),
    (NO, _(NO)),
)

YES_NO_DWTA = (
    (YES, _(YES)),
    (NO, _(NO)),
    (DWTA, _('Don\'t want to answer')),
)

YES_NO_NA = (
    (YES, YES),
    (NO, NO),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_NA_DWTA = (
    (YES, _(YES)),
    (NO, _(NO)),
    (DWTA, _('Don\'t want to answer')),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_MC_NA = (
    (YES, _(YES)),
    (NO, _(NO)),
    ('MARRIAGE CERTIFICATE'),
    ('Not applicable'),
)
