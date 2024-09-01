# Generated by Django 4.2.15 on 2024-09-01 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Webinar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('speaker', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('duration', models.DurationField(help_text='Duration of the webinar')),
                ('is_recorded', models.BooleanField(default=False)),
                ('recorded_file', models.FileField(blank=True, null=True, upload_to='webinars/recordings/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebinarRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('attended', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='webinar_registrations', to=settings.AUTH_USER_MODEL)),
                ('webinar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='webinars.webinar')),
            ],
        ),
        migrations.CreateModel(
            name='WebinarFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('rating', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('webinar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='webinars.webinar')),
            ],
        ),
    ]
