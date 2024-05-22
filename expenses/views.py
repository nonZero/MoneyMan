from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Expense


def expense_list(request: HttpRequest):
    qs = Expense.objects.order_by("-date")

    if q := request.GET.get('q'):
        qs = qs.filter(title__icontains=q)

    return render(
        request,
        "expenses/expense_list.html",
        {
            "object_list": qs[:20],
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
