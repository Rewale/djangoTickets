# Generated by Django 3.2.7 on 2021-10-05 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_customer_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aircompany',
            options={'verbose_name': 'Аэропорт', 'verbose_name_plural': 'Аэропорты'},
        ),
        migrations.AlterModelOptions(
            name='airport',
            options={'verbose_name': 'Аэропорт', 'verbose_name_plural': 'Аэропорты'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Страна', 'verbose_name_plural': 'Страны'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Покупатель', 'verbose_name_plural': 'Покупатели'},
        ),
        migrations.AlterModelOptions(
            name='flight',
            options={'verbose_name': 'Рейс', 'verbose_name_plural': 'Рейсы'},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'Билет', 'verbose_name_plural': 'Билеты'},
        ),
        migrations.AlterModelOptions(
            name='town',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='Miles',
        ),
        migrations.AddField(
            model_name='flight',
            name='Miles',
            field=models.FloatField(default=0, verbose_name='Количетсво миль'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='tickets.aircompany', verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='DateFrom',
            field=models.DateTimeField(verbose_name='Время вылета'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='DateTo',
            field=models.DateTimeField(verbose_name='Время прилета (прибл.)'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Flight_ID',
            field=models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Номер рейса'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='airFrom',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='airFrom', to='tickets.airport', verbose_name='Вылет из'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='airTo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='airTo', to='tickets.airport', verbose_name='Прилет в'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='Customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer', to='tickets.customer', verbose_name='Покупатель'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='FlightOfTicket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='tickets.flight'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='Seat',
            field=models.CharField(max_length=5, verbose_name='Место'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='Seq',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, verbose_name='Номер'),
        ),
    ]