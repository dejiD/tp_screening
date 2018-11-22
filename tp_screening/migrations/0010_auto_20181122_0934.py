# Generated by Django 2.1.2 on 2018-11-22 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tp_screening', '0009_auto_20181121_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='literacy_status',
            field=models.CharField(choices=[('YES', 'literate'), ('NO', 'illiterate')], max_length=15, verbose_name='13. Are you Literate?'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='literacy_status',
            field=models.CharField(choices=[('YES', 'literate'), ('NO', 'illiterate')], max_length=15, verbose_name='13. Are you Literate?'),
        ),
    ]