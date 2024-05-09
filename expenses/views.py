import calendar
import random

from django.http import HttpRequest
from django.shortcuts import render

from .models import Expense


def expense_list(request: HttpRequest):
    cal = calendar.HTMLCalendar()
    return render(
        request,
        "expenses/expense_list.html",
        {
            "month": cal.formatmonth(2022, 5),
            "object_list": Expense.objects.order_by("-date")[:20],
        },
    )
