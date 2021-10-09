# Generated by Django 3.2.7 on 2021-10-09 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0007_alter_aircompany_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Miles',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='Customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_tickets', to='tickets.customer', verbose_name='Покупатель'),
        ),
        migrations.AlterUniqueTogether(
            name='customer',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('document', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('birthDate', models.DateField(verbose_name='День рождения')),
                ('FIO', models.CharField(max_length=100)),
                ('citizenship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citizens', to='tickets.country')),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='FIO',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='passportNum',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='passportSeries',
        ),
        migrations.AddField(
            model_name='customer',
            name='passenger',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, to='tickets.passenger'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='Passenger',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='tickets.passenger', verbose_name='Пассажир'),
        ),
    ]