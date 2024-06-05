from django.urls import path

from . import views
from .views import ExpenseListView

app_name = "expenses"

urlpatterns = [
    path("", ExpenseListView.as_view(), name="list"),
    path("add/", views.expense_create, name="create"),
    path("expense/<int:pk>/", views.ExpenseDetailView.as_view(), name="detail"),
]
