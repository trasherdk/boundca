# Generated by Django 4.0.4 on 2022-05-28 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_authorisedapp_scopes_delete_scope'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authorisedapp',
            old_name='owner',
            new_name='user',
        ),
    ]
