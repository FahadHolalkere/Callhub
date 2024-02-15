# tickets/urls.py
from django.urls import path
from .views import ticket_list, ticket_detail, ticket_add, create_ticket ,update_ticket, ticket_edit, ticket_closed, search

urlpatterns = [
    path('', ticket_list, name='ticket_list'),
    path('search/', search, name='search'),
    path('closed/', ticket_closed, name='ticket_closed'),
    path('closed/detail/<int:pk>/', ticket_detail, name='ticket_detail'),
    path('detail/<int:pk>/', ticket_detail, name='ticket_detail'),
    path('edit/<int:pk>/', ticket_edit, name='ticket_edit'),
    path('add/', ticket_add , name='ticket_add'),
    path('created/', create_ticket , name='create_ticket'),
    path('updated/<int:pk>/', update_ticket , name='update_ticket'),
]
