from django.contrib.auth.models import User
from django.db import models


class AirCompany(models.Model):
    """Авиакомпания - поставщик билетов"""
    icon = models.ImageField()
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Аэропорт'
        verbose_name_plural = 'Аэропорты'

    def __str__(self):
        return f'{self.name}'


class Country(models.Model):
    """Страна"""
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return f'{self.name}'


class Town(models.Model):
    """Город"""
    name = models.CharField(max_length=100)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE, related_name="country")

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.name}, {self.country}'


class Airport(models.Model):
    """Аэропорт"""
    IATA_code = models.CharField(max_length=3, primary_key=True)
    town = models.ForeignKey(to=Town, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Аэропорт'
        verbose_name_plural = 'Аэропорты'

    def __str__(self):
        return f'{self.IATA_code}({self.town})'


class Flight(models.Model):
    """Рейс"""
    Flight_ID = models.CharField(max_length=6, primary_key=True, verbose_name="Номер рейса")
    DateFrom = models.DateTimeField(verbose_name="Время вылета")
    DateTo = models.DateTimeField(verbose_name="Время прилета (прибл.)")
    # Gate = models.DateTimeField()
    # CountOfTickets = models.IntegerField()
    airFrom = models.ForeignKey(to=Airport, on_delete=models.CASCADE, related_name="airFrom", verbose_name="Вылет из"
                                , default=None)
    airTo = models.ForeignKey(to=Airport, on_delete=models.CASCADE, related_name='airTo', verbose_name="Прилет в"
                              , default=None)
    Company = models.ForeignKey(to=AirCompany, on_delete=models.CASCADE, related_name='company',
                                verbose_name="Компания")
    Miles = models.FloatField(verbose_name="Количетсво миль", default=0)

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'

    def __str__(self):
        return f'{self.Flight_ID}'


# TODO:Сделать кастомного юзера
class Customer(models.Model):
    """Покупатель"""

    class Meta:
        unique_together = (('passportSeries', 'passportNum'),)
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    passportSeries = models.CharField(max_length=4, primary_key=True)
    passportNum = models.CharField(max_length=6)
    user = models.ForeignKey(to=User,
                             default=User.objects.get(pk=1).pk,
                             on_delete=models.CASCADE,
                             related_name='posts')
    FIO = models.CharField(max_length=100)
    # Miles = models.FloatField()

    def __str__(self):
        return f'{self.user.pk}:{self.FIO}'


class Ticket(models.Model):
    """Билет"""

    class Meta:
        unique_together = (('Seq', 'FlightOfTicket'),)
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

    FlightOfTicket = models.ForeignKey(to=Flight, on_delete=models.CASCADE, related_name='tickets')

    Seq = models.IntegerField(primary_key=True, verbose_name="Номер",
                              default=1)

    Cost = models.IntegerField(verbose_name="Цена")
    Seat = models.CharField(max_length=5, verbose_name="Место")
    Customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, verbose_name="Покупатель",
                                 related_name="Customer")

    def __str__(self):
        return f'{self.FlightOfTicket}:{self.Seat}'
