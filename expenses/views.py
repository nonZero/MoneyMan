import datetime

from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Expense


def expense_list(request: HttpRequest):
    qs = Expense.objects.order_by("-date")

    if q := request.GET.get('q', ''):
        qs = qs.filter(title__icontains=q)

    if recent_only := request.GET.get('recent_only', '') == "on":
        d = datetime.date.today() - datetime.timedelta(days=90)
        qs = qs.filter(date__gte=d)

    return render(
        request,
        "expenses/expense_list.html",
        {
            "object_list": qs[:20],
            "q": q,
            "recent_only": recent_only,
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
