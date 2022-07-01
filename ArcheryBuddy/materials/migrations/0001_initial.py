# Generated by Django 4.0.5 on 2022-07-01 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nock', models.CharField(max_length=60)),
                ('feathering_type', models.CharField(choices=[('VANES', 'pennes'), ('SPINWINGS', 'spin wings'), ('FEATHERS', 'plumes'), ('FLUFLU', 'flu-flu')], default=('VANES', 'pennes'), max_length=10)),
                ('feathering_brand', models.CharField(max_length=60)),
                ('feathering_color', models.CharField(max_length=60)),
                ('feathering_cock_color', models.CharField(max_length=60)),
                ('feathering_size', models.CharField(max_length=60)),
                ('feathering_angle', models.IntegerField()),
                ('feathering_nock_distance', models.IntegerField()),
                ('tip_brand', models.CharField(max_length=60)),
                ('tip_profile', models.CharField(max_length=60)),
                ('tip_weight', models.CharField(max_length=60)),
                ('tube_brand', models.CharField(max_length=60)),
                ('tube_length', models.FloatField()),
                ('tube_spine', models.FloatField()),
                ('tube_diameter', models.FloatField()),
                ('not_broken', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user', verbose_name='user')),
            ],
        ),
    ]
