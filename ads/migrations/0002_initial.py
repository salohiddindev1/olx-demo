# Generated by Django 5.1.6 on 2025-03-12 04:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ads', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='reklama',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reklamalar', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reklamaimages',
            name='reklama',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rasimlar', to='ads.reklama'),
        ),
    ]
