# Generated by Django 4.2.7 on 2023-12-14 16:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_userprofile_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
