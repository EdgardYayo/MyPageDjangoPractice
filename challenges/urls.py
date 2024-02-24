from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month_number>", views.monthly_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]