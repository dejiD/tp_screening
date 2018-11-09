'''
Created on 05 Oct 2018

@author: Deji
'''
import re

ABNORMAL = 'ABNORMAL'
ADDITIONAL = True
AFTERNOON = 'afternoon'
ALIVE = 'alive'
ANONYMOUS = 'anonymous'
ANYTIME = 'anytime'
BY_BIRTH = 'BY_BIRTH'
CANCELLED = 'cancelled'
CLOSED = 'closed'
COMPLETE = 'COMPLETE'
CONSENTED = 'consented'
CONTINUOUS = 'continuous'
DEAD = 'dead'
DECLINED = 'Declined'
DEFAULTER = 'defaulter'
DELETE = 'DELETE'
DONE = 'done'
DONT_KNOW = 'dont_know'
DWTA = 'DWTA'  # don't want to answer'
ERROR = 'ERROR'
EVENING = 'evening'
FAILED_ELIGIBILITY = 'failed eligibility'
FEMALE = 'F'
HIDE_FORM = 'NOT_REQUIRED'
INCOMPLETE = 'INCOMPLETE'
IND = 'IND'
INSERT = 'INSERT'
LOST_TO_FOLLOWUP = 'LTFU'
MALE = 'M'
MORNING = 'morning'
NAIVE = 'NAIVE'
NEG = 'NEG'
NEVER = 'NEVER'
NEW = 'New'
NO = 'No'
NONE = 'none'
NORMAL = 'NORMAL'
NOT_ADDITIONAL = False
NOT_APPLICABLE = 'N/A'
NOT_DONE = 'not_done'
NOT_EVALUATED = 'Not evaluated'
NOT_SURE = 'not_sure'
OFF_STUDY = 'off study'
OFF_STUDY_VISIT = 'off study'
OMANG = 'OMANG'
ON_ART = 'on_art'
ON_STUDY = 'on study'
OPEN = 'open'
OPTIONAL = True
OTHER = 'OTHER'
PARTIAL = 'PARTIAL'
PARTICIPANT = 'participant'
PENDING = 'PENDING'
POS = 'POS'
PRINT = 'PRINT'
QUERY = 'QUERY'
REFUSED = 'REFUSED'
RESTARTED = 'restarted'
SCREENED = 'SCREENED'
SEROCONVERSION = 'seroconversion'
SHOW_FORM = 'NEW'
STOPPED = 'stopped'
SUBJECT = 'subject'
UNK = 'UNK'
UNKNOWN = 'unknown'
UPDATE = 'UPDATE'
UUID_PATTERN = re.compile(
    '[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}')
VIEW = 'VIEW'
WEEKDAYS = 'weekdays'
WEEKENDS = 'weekends'
YES = 'Yes'
VERY_ACTIVE = 'VERY_ACTIVE'
SOMEWHAT_ACTIVE = 'SOMEWHAT_ACTIVE'
NOT_ACTIVE_AT_ALL = 'NOT_ACTIVE_AT_ALL'
DO_NOT_WANT_TO_ANSWER = 'DWTA'
FARMER = 'FARMER'
FARM_WORKER = 'FARM_WORKER'
DOMESTIC_WORKER = 'DOMESTIC_WORKER'
PRIVATE_WORKER = 'PRIVATE_WORKER'
FISHING = 'FISHING'
MINING = 'MINING'
TOURISM = 'TOURISM'
SME = 'SME'
INFORMAL_SELLING = 'INFORMAL_SELLING'
COMMERCIAL_SEX_WORKER = 'COMMERCIAL_SEX_WORKER'
TRANSPORT = 'TRANSPORT'
FACTORY = 'FACTORY'
GAURD = 'GAURD'
POLICE_SOLDIER = 'POLICE_SOLDIER'
CLERK = 'CLERK'
GOVERNMENT_WORKER = 'GOVERNMENT_WORKER'
TEACHER = 'TEACHER'
HEALTHCARE_WORKER = 'HEALTHCARE_WORKER'
OTHER_PROFESSIONAL = 'OTHER_PROFESSIONAL'
SINGLE = 'SINGLE'
MARRIED = 'MARRIED'
MARRIAGE_CERTIFICATE = 'MARRIAGE_CERTIFICATE'
DIVORCED = 'DIVORCED'
WIDOWED = 'WIDOWED'
HIV_AIDS = 'HIV_AIDS'
Schools = 'Schools'
Sewer = 'Sewer'
Unemployment = 'Unemployment'
Roads = 'Roads'
Water = 'Water'
Other_specify = 'Other_specify'
House = 'House'
Malaria = 'Malaria'
NO = 'NO'
NOT_APPLICABLE = 'NOT_APPLICABLE'
YES = 'YES'
Occassional_CasualEmployment = 'Occassional_CasualEmployment_(piece_job)'
Seasonal_Employment = 'Seasonal_Employment'
Formal_Wage_Employment = 'Formal_Wage_Employment(full-time)'
Formal_Wage_Employment = 'FormalWageEmployment(part-time)'
Self_Employed_Agriculture = 'Self_Employed_Agriculture'
Self_employed_Making_Money = 'Self_employed_Making_Money(full time)'
Self_Employed_Making_Money = 'Self_Employed_Making_Money(part time)'

BOTSWANA = 'BOTSWANA'
PARTNER_SPOUSE = 'PARTNER_SPOUSE'
NO_ANSWER = 'NO_ANSWER'
ALONE = 'ALONE'

Level_one = '1-199 pula'
Level_two = '200-499 pula'
Level_three = '500-999 pula'
Level_four = '1000-4999 pula'
Level_five = '5000-10,000 pula'
Level_six = 'More than 10,000 pula'

Literate_Witness = 'Literate Witness'
GAURDIAN_PRESENT = 'GAURDIAN PRESENT'
