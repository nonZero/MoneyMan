import random

from django.http import HttpRequest
from django.shortcuts import render

from .models import Expense


def expense_list(request: HttpRequest):
    # qs = Expense.objects.all()
    n = random.randint(1, 100)
    colors = ["purple", "green", "blue"]
    foo = 12345
    person = {"name": "aviv", "phone": "1234567"}
    return render(
        request,
        "expenses/expense_list.html",
        {
            "colors": colors,
            "mashu": foo,
            "kuku": "abcdefg",
            "p": person,
            "n": n,
        },
    )
