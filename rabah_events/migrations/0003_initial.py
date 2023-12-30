# Generated by Django 4.2.7 on 2023-12-09 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rabah_events', '0002_initial'),
        ('rabah_organisations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberattendance',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rabah_organisations.organisation'),
        ),
        migrations.AddField(
            model_name='eventmember',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rabah_events.event'),
        ),
        migrations.AddField(
            model_name='eventmember',
            name='members_attendance',
            field=models.ManyToManyField(blank=True, to='rabah_events.memberattendance'),
        ),
        migrations.AddField(
            model_name='eventmember',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rabah_organisations.organisation'),
        ),
        migrations.AddField(
            model_name='event',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rabah_organisations.organisation'),
        ),
    ]