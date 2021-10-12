from rest_framework import serializers
from . import models


class TicketSerializer(serializers.ModelSerializer):
    """Список билетов"""
    class Meta:
        model = models.Ticket
        fields = ('FlightOfTicket', 'Seq', 'Cost', 'Seat')
