from django.urls import path, include
from . import views
urlpatterns = [
    path("tickets/", views.TicketsListView.as_view()),
]