# Generated by Django 4.0.4 on 2022-05-05 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=64, null=True)),
                ('province', models.CharField(blank=True, max_length=64, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=12, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Annotator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abstract_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.abstractuser')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abstract_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.abstractuser')),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issuer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.company')),
            ],
        ),
        migrations.CreateModel(
            name='Datum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=256)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dataset')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=256)),
                ('points', models.FloatField()),
                ('completed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.annotator')),
                ('datum', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.datum')),
            ],
        ),
    ]
