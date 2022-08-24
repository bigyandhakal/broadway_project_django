# Generated by Django 4.0.4 on 2022-07-14 04:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_date', models.DateField(default=datetime.datetime(2022, 7, 14, 4, 57, 14, 645636, tzinfo=utc))),
                ('status', models.CharField(choices=[('Applied', 'Applied'), ('Review', 'Review'), ('Selected', 'Selected'), ('Rejected', 'Rejected'), ('Waiting', 'Waiting')], max_length=255)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
