from rest_framework import serializers
from . import models


class TicketSerializer(serializers.ModelSerializer):
    """Список билетов"""

    class Meta:
        model = models.Ticket
        fields = ('FlightOfTicket', 'Seq', 'Cost', 'Seat')


# TODO: серилизовать компанию
class FlightSerializer(serializers.ModelSerializer):
    """Список рейсов"""
    count_tickets = serializers.IntegerField()

    class Meta:
        model = models.Flight
        fields = ('Flight_ID', 'DateFrom', 'DateTo', 'airFrom', 'airTo', 'Company', 'count_tickets')
