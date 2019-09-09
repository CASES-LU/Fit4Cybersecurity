# Generated by Django 2.2.3 on 2019-09-09 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_tel', models.TextField(max_length=32)),
                ('contact_address_street', models.CharField(max_length=128)),
                ('contact_address_city', models.CharField(max_length=64)),
                ('contact_address_country', models.CharField(choices=[('LU', 'Luxembourg'), ('DE', 'Deutschland'), ('BE', 'Belgique'), ('FR', 'France')], max_length=2)),
                ('contact_address_number', models.IntegerField()),
                ('contact_address_postcode', models.CharField(max_length=10)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SurveyAnswerRecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendation', models.TextField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.SurveyQuestionAnswer')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(choices=[('SME', 'Small to Medium Size Entreprises'), ('BC', 'Big Company'), ('MN', 'Multinationals Coorporations'), ('IND', 'Independent'), ('PRI', 'Private Person')], max_length=3)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.SurveyQuestionServiceCategory')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveySummary.Company')),
            ],
        ),
    ]
