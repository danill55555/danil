# Generated by Django 5.0.6 on 2024-05-22 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Violations', '0002_role_user_roles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='status',
            new_name='roles',
        ),
    ]