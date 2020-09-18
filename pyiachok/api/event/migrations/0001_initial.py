# Generated by Django 3.1 on 2020-08-28 09:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_auth', '0001_initial'),
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyiachokModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('purpose', models.CharField(max_length=150)),
                ('sex', models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^([fma])$', 'only f/m/a')])),
                ('number_of_people', models.IntegerField()),
                ('payer', models.CharField(max_length=20)),
                ('expenditures', models.IntegerField()),
                ('public', models.BooleanField(default=True)),
                ('participants', models.ManyToManyField(related_name='active_pyiachky', to='user_auth.ProfileModel')),
                ('place_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pyiachky', to='place.placemodel')),
                ('requests', models.ManyToManyField(related_name='pyiachok_requests', to='user_auth.ProfileModel')),
            ],
            options={
                'db_table': 'pyiachok',
            },
        ),
    ]
