from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models as models_app
from django.db import models
# Create your views here.
from .serializers import TicketSerializer, FlightSerializer


# TODO: АВТОРИЗАЦИЯ/РЕГИСТРАЦИЯ
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


class UsersTickets(generics.ListAPIView):
    """Список билетов купленных пользователем"""
    serializer_class = TicketSerializer
    # permission_classes =

    def get_queryset(self):
        customer = models_app.Customer.objects.filter(user=self.request.user.pk).first()
        print(customer)

        tickets = models_app.Ticket.objects.filter(Customer=customer)

        return tickets


@api_view(('GET',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def buy_ticket(request, flight_num, seq):

    ticket = models_app.Ticket.objects.get(FlightOfTicket=flight_num, Seq=seq)

    if ticket.Customer is not None:
        return Response(data='Response=Neok,error=Билет уже куплен')

    ticket.Customer = models_app.Customer.objects.first()
    ticket.save()

    return Response(data="ok")
