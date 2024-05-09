from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Expense


def expense_list(request: HttpRequest):
    return render(
        request,
        "expenses/expense_list.html",
        {
            "object_list": Expense.objects.order_by("-date")[:20],
        },
    )


def expense_detail(request: HttpRequest, id: int):
    return render(
        request,
        "expenses/expense_detail.html",
        {
            "object": get_object_or_404(Expense, id=id),
        },
    )
