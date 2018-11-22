# Generated by Django 2.1.2 on 2018-10-31 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tp_screening', '0004_auto_20181031_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectscreening',
            name='job_description',
            field=models.CharField(choices=[('FARMER', 'farmer (own land)'), ('FARM_WORKER', 'farm work on employers land'), ('DOMESTIC_WORKER', 'domestic worker'), ('PRIVATE_WORKER', 'work in bar/ hotel/guest house/ entertainment venue'), ('FISHING', 'fishing'), ('MINING', 'mining'), ('TOURISM', 'tourism/game parks'), ('SME', 'working in shop / small business'), ('INFORMAL_SELLING', 'informal selling'), ('COMMERCIAL_SEX_WORKER', 'commercial sex work'), ('TRANSPORT', 'transport (trucker/ taxi driver)'), ('FACTORY', 'factory worker'), ('GAURD', 'guard (security company)'), ('POLICE_SOLDIER', 'police/Soldier'), ('CLERK', 'clerical and office work'), ('GOVERNMENT_WORKER', 'government worker'), ('TEACHER', 'teacher'), ('HEALTHCARE_WORKER', 'health care worker'), ('OTHER_PROFESSIONAL', 'other professional'), ('DWTA', 'do not want to answer'), ('OTHER', 'other')], default=False, max_length=35, verbose_name='12. Describe the work that you do or did in your most recent job.If you have more than one profession,choose the one you spend the most time doing'),
        ),
        migrations.AddField(
            model_name='subjectscreening',
            name='job_income',
            field=models.CharField(choices=[('NONE', 'none'), ('Level_one', '1-199 pula'), ('Level_two', '200-499 pula'), ('Level_three', '500-999 pula'), ('Level_four', '1000-4999 pula'), ('Level_five', '5000-10,000 pula'), ('Level_six', 'more than 10,000 pula'), ('DWTA', 'do not want to answer')], default=False, max_length=35, verbose_name='11. In the past month, how much money did you earnfrom work you did or received in payment?'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='age_in_years',
            field=models.CharField(choices=[('None', 'None'), ('0-17', '0-17'), ('18 and above', '18 and above')], max_length=15, verbose_name='1. How old are you?'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='citizen_of_Botswana',
            field=models.CharField(choices=[('YES', 'yes'), ('NO', 'no')], max_length=15, verbose_name='5. Are you a citizen of Botswana?'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='gaurdian_present',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('NA', 'not applicable')], max_length=35, verbose_name='4. Do you have a gaurdian present?'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='gender',
            field=models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female')], max_length=15, verbose_name='2. Select your Gender'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='job_details',
            field=models.CharField(choices=[('Occassional_CasualEmployment', 'occassional_casualemployment(piece_job)'), ('Seasonal_Employment', 'seasonal_employment'), ('Formal_Wage_Employment', 'formal_wage_employment(full-time)'), ('Formal_Wage_Employment', 'formal_wage_employment(part-time)'), ('Self_Employed_Agriculture', 'self_employed_agriculture'), ('Self_employed_Making_Money', 'self_employed_making_money(full time)'), ('Self_employed_Making_Money', 'self_employed_making_money(part time)'), ('DWTA', 'do not want to answer'), ('OTHER', 'other')], max_length=35, verbose_name='10. In your main job what type of work do you do?'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='job_status',
            field=models.CharField(choices=[('YES', 'yes'), ('NO', 'no'), ('DNWTA', 'do not want to answer')], max_length=35, verbose_name='9. Are you currently working?'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='literacy_status',
            field=models.CharField(choices=[('LITERATE', 'literate'), ('ILLETERATE', 'illeterate')], max_length=15, verbose_name='13. Are you Literate?'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='literate_witness',
            field=models.CharField(choices=[('YES', 'yes'), ('NO', 'no'), ('NA', 'not applicable')], max_length=35, verbose_name='14. Do you have a Literate witness?'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='marital_status',
            field=models.CharField(choices=[('SINGLE', 'Single'), ('MARRIED', 'Married'), ('DIVORCED', 'Divorced'), ('WIDOWED', 'Widowed')], max_length=35, verbose_name='6. Are you married?'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='married_to_a_citizen',
            field=models.CharField(choices=[('YES', 'yes'), ('NO', 'no'), ('NA', 'not_applicable')], max_length=35, verbose_name='7. Are you married to a Motswana?'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='minor',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('NA', 'not applicable')], max_length=35, verbose_name='3.Are you in the minor category?'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='proof_of_marriage',
            field=models.CharField(choices=[('YES', 'yes'), ('NO', 'no'), ('NA', 'not_applicable')], max_length=35, verbose_name='8. Do you have a proof of marriage?'),
        ),
    ]