from django.urls import path

from . import views
from .views import ExpenseListView

app_name = "expenses"

urlpatterns = [
    path("", ExpenseListView.as_view(), name="list"),
    path("add/", views.ExpenseCreateView.as_view(), name="create"),
    path("expense/<int:pk>/", views.ExpenseDetailView.as_view(), name="detail"),
    path("expense/<int:pk>/edit/", views.ExpenseUpdateView.as_view(), name="update"),
    path("expense/<int:pk>/delete/", views.ExpenseDeleteView.as_view(), name="delete"),
]
