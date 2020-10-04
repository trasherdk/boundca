# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-13 23:42
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('x509_pki', '0006_auto_20180617_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='dn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='x509_pki.DistinguishedName'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='parent',
            field=models.ForeignKey(blank=True, help_text='The signing authority (None for root certificate)', null=True, on_delete=django.db.models.deletion.PROTECT, to='x509_pki.Certificate'),
        ),
    ]
