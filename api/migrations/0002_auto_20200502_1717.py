# Generated by Django 3.0.3 on 2020-05-02 15:17

import api.models.user
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='Teacher',
            field=models.ForeignKey(limit_choices_to={'user_type': 'TECH'}, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subject',
            name='credit_hours',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Category'),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.user.user_directory_path),
        ),
        migrations.AlterField(
            model_name='user',
            name='ssn',
            field=models.CharField(default='000000000000000', max_length=15, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(14), django.core.validators.MaxLengthValidator(14), django.core.validators.RegexValidator('^[0-9]+$', 'Only numbers are allowed.')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Stage'),
        ),
    ]