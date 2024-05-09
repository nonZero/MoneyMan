import random

from django.http import HttpRequest
from django.shortcuts import render

from .models import Expense


def expense_list(request: HttpRequest):
    # qs = Expense.objects.all()
    return render(
        request,
        "expenses/expense_list.html",
        {
            "nums": [(i, i**2) for i in range(10)],
            "grays": range(0, 256, 16),
        },
    )
