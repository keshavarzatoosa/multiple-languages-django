# Generated by Django 5.1.4 on 2025-02-04 12:01

import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_date_alter_course_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
        migrations.RemoveField(
            model_name='course',
            name='price',
        ),
        migrations.RemoveField(
            model_name='course',
            name='title',
        ),
        migrations.CreateModel(
            name='CourseTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=90)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='course.course')),
            ],
            options={
                'verbose_name': 'course Translation',
                'db_table': 'course_course_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases = (parler.models.TranslatableModel, models.Model)
        ),
    ]
