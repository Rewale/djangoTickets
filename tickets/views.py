from django.shortcuts import render
from rest_framework import generics, permissions

from . import models as models_app
from django.db import models
# Create your views here.
from .serializers import TicketSerializer


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
