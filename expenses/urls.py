from django.urls import path

from . import views

urlpatterns = [
    path("", views.expense_list),
    path("<int:id>/", views.expense_detail),
]
