from django.db import models

# Create your models here.


class AirCompany(models.Model):
    icon = models.ImageField()
    name = models.CharField(max_length=50)


class Country(models.Model):
    name = models.CharField(max_length=100)


class Town(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE, related_name="country")


class Airports(models.Model):
    IATA_code = models.CharField(max_length=3, primary_key=True)
    town = models.ForeignKey(to=Town, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)


class Flight(models.Model):
    Flight_ID = models.CharField(max_length=6, primary_key=True)
    DateFrom = models.DateTimeField()
    DateTo = models.DateTimeField()
    # Gate = models.DateTimeField()
    CountOfTickets = models.IntegerField()
    airFrom = models.ForeignKey(to=Airports, on_delete=models.CASCADE, related_name="airFrom")
    airTo = models.ForeignKey(to=Airports, on_delete=models.CASCADE, related_name='airTo')
    Company = models.ForeignKey(to=AirCompany, on_delete=models.CASCADE, related_name='company')


class Customers(models.Model):
    class Meta:
        unique_together = (('passportSeries', 'passportNum'),)
    passportSeries = models.CharField(max_length=4, primary_key=True)
    passportNum = models.CharField(max_length=6)

    FIO = models.CharField(max_length=100)
    Miles = models.FloatField()


class Tickets(models.Model):
    class Meta:
        unique_together = (('Seq', 'FlightOfTicket'),)

    Seq = models.IntegerField(primary_key=True)
    FlightOfTicket = models.ForeignKey(to=Flight, on_delete=models.CASCADE, related_name='flight')
    Cost = models.IntegerField()
    Seat = models.CharField(max_length=5)
    Customer = models.ForeignKey(to=Customers, on_delete=models.CASCADE)



