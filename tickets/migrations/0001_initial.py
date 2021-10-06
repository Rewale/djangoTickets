# Generated by Django 3.2.7 on 2021-10-03 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('IATA_code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('passportSeries', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('passportNum', models.CharField(max_length=6)),
                ('FIO', models.CharField(max_length=100)),
            ],
            options={
                'unique_together': {('passportSeries', 'passportNum')},
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('Flight_ID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('DateFrom', models.DateTimeField()),
                ('DateTo', models.DateTimeField()),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='tickets.aircompany')),
                ('airFrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airFrom', to='tickets.airport')),
                ('airTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airTo', to='tickets.airport')),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country', to='tickets.country')),
            ],
        ),
        migrations.AddField(
            model_name='airport',
            name='town',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.town'),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('Miles', models.FloatField()),
                ('Seq', models.IntegerField(primary_key=True, serialize=False)),
                ('Cost', models.IntegerField(verbose_name='Цена')),
                ('Seat', models.CharField(max_length=5)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.customer')),
                ('FlightOfTicket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight', to='tickets.flight')),
            ],
            options={
                'unique_together': {('Seq', 'FlightOfTicket')},
            },
        ),
    ]
