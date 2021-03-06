# Generated by Django 4.0.1 on 2022-01-29 06:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('isDriver', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('departure', models.CharField(max_length=32)),
                ('arrival', models.CharField(max_length=32)),
                ('specialText', models.TextField(blank=True, default='')),
                ('isConfirmed', models.BooleanField(default=False)),
                ('isSharable', models.BooleanField(default=False)),
                ('driverWho', models.CharField(max_length=32)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='ride.user')),
                ('sharer', models.ManyToManyField(related_name='sharer', to='ride.User')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.CharField(max_length=32)),
                ('license', models.CharField(max_length=32)),
                ('seats', models.IntegerField()),
                ('specialText', models.TextField(blank=True, default='')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ride.user')),
            ],
        ),
    ]
