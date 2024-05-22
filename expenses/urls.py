from django.urls import path

from . import views

app_name = "expenses"

urlpatterns = [
    path("", views.expense_list, name="list"),
    path("expense/<int:id>/", views.expense_detail, name="detail"),
]
