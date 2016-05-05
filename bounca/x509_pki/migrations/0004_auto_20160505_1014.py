# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 08:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('x509_pki', '0003_auto_20160505_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='name',
            field=models.CharField(blank=True, help_text='Long name of your authority, if not set will be equal to your shortname + CommonName.', max_length=128, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z@#$%^&+=\\_\\.\\-\\,\\ ]*$', 'Only alphanumeric characters and [@#$%^&+=_,-.] are allowed.')]),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='x509_pki.Certificate'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='shortname',
            field=models.CharField(help_text='Short name used to store your keys and scripts.', max_length=128, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z\\_\\.]*$', 'Only alphanumeric characters and [_.] are allowed.')]),
        ),
    ]
