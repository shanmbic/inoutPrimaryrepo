# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=3000)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=500)),
                ('timestamp', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('type_user', models.CharField(max_length=30)),
                ('first', models.CharField(max_length=30)),
                ('current_location', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='messages',
            name='user',
            field=models.OneToOneField(to='core.UserProfile'),
        ),
        migrations.AddField(
            model_name='documents',
            name='user_belong',
            field=models.OneToOneField(related_name='UserCreatedFrom', to='core.UserProfile'),
        ),
        migrations.AddField(
            model_name='documents',
            name='user_shared',
            field=models.OneToOneField(related_name='UserSharedWith', to='core.UserProfile'),
        ),
    ]
