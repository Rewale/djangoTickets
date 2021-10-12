from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models as models_app
from django.db import models
# Create your views here.
from .serializers import TicketSerializer, FlightSerializer


class TicketsListView(generics.ListAPIView):
    """Вывод списка билетов"""
    serializer_class = TicketSerializer

    # filter_backends = (DjangoFilterBackend,)
    # filterset_class = service.MovieFilter
    # permission_classes = [permissions.IsAuthenticated]

    # Не выводим купленные билеты
    def get_queryset(self):
        tickets = models_app.Ticket.objects.filter(Customer=None)

        return tickets


# TODO: нормально передавать параметры в запросе
class TicketsInFlightListView(APIView):
    """Вывод билетов определенного рейса"""

    def get(self, request,):
        flight_num = request.GET.get("flight", "")

        if flight_num:
            tickets = models_app.Ticket.objects.filter(FlightOfTicket=flight_num, Customer=None)
        else:
            tickets = models_app.Ticket.objects.filter(Customer=None)
        serializer = TicketSerializer(tickets, many=True)

        return Response(serializer.data)


class FlightListView(generics.ListAPIView):
    serializer_class = FlightSerializer

    def get_queryset(self):
        flights = models_app.Flight.objects.annotate(count_tickets=models.Count('tickets'))

        return flights