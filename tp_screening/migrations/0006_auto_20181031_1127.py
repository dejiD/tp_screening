# Generated by Django 2.1.2 on 2018-10-31 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tp_screening', '0005_auto_20181031_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectscreening',
            name='job_description',
            field=models.CharField(choices=[('FARMER', 'farmer (own land)'), ('FARM_WORKER', 'farm work on employers land'), ('DOMESTIC_WORKER', 'domestic worker'), ('PRIVATE_WORKER', 'work in bar/ hotel/guest house/ entertainment venue'), ('FISHING', 'fishing'), ('MINING', 'mining'), ('TOURISM', 'tourism/game parks'), ('SME', 'working in shop / small business'), ('INFORMAL_SELLING', 'informal selling'), ('COMMERCIAL_SEX_WORKER', 'commercial sex work'), ('TRANSPORT', 'transport (trucker/ taxi driver)'), ('FACTORY', 'factory worker'), ('GAURD', 'guard (security company)'), ('POLICE_SOLDIER', 'police/Soldier'), ('CLERK', 'clerical and office work'), ('GOVERNMENT_WORKER', 'government worker'), ('TEACHER', 'teacher'), ('HEALTHCARE_WORKER', 'health care worker'), ('OTHER_PROFESSIONAL', 'other professional'), ('DWTA', 'do not want to answer'), ('OTHER', 'other')], max_length=35, verbose_name='12. Describe the work that you do or did in your most recent job.If you have more than one profession,choose the one you spend the most time doing'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='job_income',
            field=models.CharField(choices=[('NONE', 'none'), ('Level_one', '1-199 pula'), ('Level_two', '200-499 pula'), ('Level_three', '500-999 pula'), ('Level_four', '1000-4999 pula'), ('Level_five', '5000-10,000 pula'), ('Level_six', 'more than 10,000 pula'), ('DWTA', 'do not want to answer')], max_length=35, verbose_name='11. In the past month, how much money did you earnfrom work you did or received in payment?'),
        ),
    ]