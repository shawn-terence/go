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
            name='FundingOpportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('sector', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('deadline', models.DateTimeField()),
                ('link', models.URLField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_sector', models.CharField(blank=True, max_length=100, null=True)),
                ('preferred_region', models.CharField(blank=True, max_length=100, null=True)),
                ('notify_by_email', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preferences', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommended_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_viewed', models.BooleanField(default=False)),
                ('funding_opportunity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='funding_recommendations.fundingopportunity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
