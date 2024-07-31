# calendar_app/urls.py
from django.urls import path
from . import views

app_name = 'calendarapp'


urlpatterns = [
    path('re', views.calendar_view, name='calendar_view'),
    path('<int:year>/<int:month>/', views.calendar_view, name='calendar_view_month'),
]
