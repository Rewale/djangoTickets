from django.contrib import admin
from . import models

#TODO:адекватное и красивое отображение всех моделей https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Admin_site
class TicketsInstanceInline(admin.TabularInline):
    model = models.Tickets

#TODO:добавление нового билета к рейсу
@admin.register(models.Flight)
class BookAdmin(admin.ModelAdmin):
    list_display = ('Flight_ID', 'DateFrom', 'DateTo', 'airTo', 'airFrom')
    inlines = [TicketsInstanceInline]

# admin.site.register(models.Tickets)
# admin.site.register(models.Customers)
# admin.site.register(models.Flight)
# admin.site.register(models.AirCompany)
# admin.site.register(models.Airports)
# admin.site.register(models.Town)
# admin.site.register(models.Country)




