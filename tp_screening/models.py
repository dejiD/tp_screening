from django.db import models
from edc_constants.choices import GENDER, YES_NO, YES_NO_NA, NORMAL_ABNORMAL
from ..subject_screening_eligibility import SubjectScreeningEligibility
from ..identifiers import ScreeningIdentifier




class tp_screening(SubjectIdentifierModelMixin, SiteModelMixin, BaseUuidModel):
    
    eligibility_cls = SubjectScreeningEligibility

    identifier_cls = ScreeningIdentifier

    age_in_years = models.IntegerField()
    
    gender = models.CharField(
        choices=GENDER,
        max_length=10)
    
    a_citizen = models.CharField(
        verbose_name='Are you a Botswana Citizen?',
        max_length=5,
        choices=YES_NO)
    
    not_a_citizen = models.CharField(
        verbose_name='Are you married to to a Motswana?',
        verbose_name='Do you have a Marriage certificate?',
        max_lenght=30,
        choices=YES_NO)
    
    eligible = models.CharField(
        verbose_name= 'Are you a Minor?',
        max_lenght=30,
        choices=Yes_NO_IHaveAGaurdian)    
    
    literacy = models.CharField(
        verbose_name='Literate , Illiterate , I Have a Literate witness',
        max_length=5,
        choices=YES_NO_LiterateWitness)
      
    '''Subject_Consent'''
    
    marital_status = models.CharField(
        verbose_name='Marital Status?',
        max_length=30,
        choices=SINGLE_MARRIED_DIVORCED_WIDOWED)
    
    address = models.CharField(
        verbose_name= 'Who do you currently live with?',
        max_lenght=30,
        choices=Alone_Partner_Spouse_Siblings_Other_NoAnswer)

    screening_identifier = models.CharField(
        verbose_name='Screening ID',
        max_length=50,
        blank=True,
        unique=True,
        editable=False)

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        help_text='Date and time of report.')

    '''Educational_Background'''

    job_status = models.CharField(
        verbose_name= 'Are you currently working?',
        max_lenght=30,
        choices=YES_NO)

    job_details = models.CharField(
        verbose_name=('In your job, what type of work do you do?'),
        max_length=20,
        job="Occassional_CasualEmployment(piece_job)"
        "Seasonal-Employment_Formal-Wage-Employment(full-time)", "FormalWageEmployment(part-time)"
        "Self-Employed_Agriculture", "Self-employed-Making-Money(full time)",
        "Self-Employed-Making-Money(part time)", "Don't-Want-To-Answer_Other",
        
        choices= job)
    
    job_description = model.CharField(
        verbose_name= ('Describe the work that you do or did in your most recent job.'
                      'If you have more than one profession,choose the one you spend the most time doing.'),
        max_lenght=30,
        job_specs="Farmer (own land)", "Farm work on employers land", "Domestic worker", 
                  "Work in bar/ hotel/ guest house/ entertainment venue",
                  "Fishing", "Mining", "Tourism/game parks", "Working in shop / small business", 
                  "Informal selling", "Commercial sex work", "Transport (trucker/ taxi driver)",
                  "Factory worker", "Guard (security company)", "Police/Soldier", 
                  "Clerical and office work", "Government worker", "Teacher", "Health care worker", 
                  "Other professional", "Don't want to answer", "Other",

        choices = job_specs)
    
    job_income = model.CharField(
        verbose_name=('In the past month, how much money did you earn from work you did or received in payment?'),
        max_lenght=30,
        monthly_income="None", "No income", "1-199 pula", "200-499 pula", "500-999 pula", "1000-4999 pula",
               "5000-10,000 pula", "More than 10,000 pula", "Don't want to answer",
        choices = monthly_income)  
    
    ''' Community_Engagement '''
    
    community_activity = models.CharField(
        verbose_name=('How active are you in community activities such as burial society, Motshelo,' 
                     'Syndicate, PTA, VDC(Village Developement Committee),' 
                     'Mophato and development of the community'),
        max_length=30,
        choices= Very-Active_Somewhat-Active_Not-Active-At-All_Dont-Want-To-Answer)
    
    voting = models.CharField(
        verbose_name=('Did you vote in the last local government election?'),
        max_length=30,
        choices= YES_NO_Not-Applicable_Dont-Want-To-Answer)
    
    
    neighborhood_problems = models.Charfield(
        verbose_name=('What are the major problems in your neighborhood ?'),
        max_lenght = 30,
        major_neighborhood_problems = "HIV/AIDS", "Schools", "Sewer", "Unemployment",
                                      "Roads", "Water", "Other","House", "Malaria",

        choices= major_neighborhood_problems)
    
    neighborhood_problems_solved = models.CharField(
        verbose_name= ('If there is a problem in this neighborhood, do the adults work together in solving it?'),
        max_lenght= 30,
        
        choices =Yes_No_Dont-know_Dont-want-to-answer)
    
