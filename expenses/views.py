import datetime

from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

from . import forms
from .models import Expense


def expense_list(request: HttpRequest):
    qs = Expense.objects.order_by("-date")

    form = forms.SearchForm(request.GET if request.GET else None)

    if form.is_valid():
        d = form.cleaned_data
        if d['q']:
            qs = qs.filter(title__icontains=d['q'])
        if d['recent_only']:
            day = datetime.date.today() - datetime.timedelta(days=90)
            qs = qs.filter(date__gte=day)
        if d['category']:
            qs = qs.filter(category=d['category'])
        qs = qs.order_by(d['sort_field'])



    return render(
        request,
        "expenses/expense_list.html",
        {
            "object_list": qs[:20],
            "form": form,
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


def expense_create(request: HttpRequest):
    if request.method == "POST":
        form = forms.ExpenseForm(request.POST)
        if form.is_valid():
            # d = form.cleaned_data
            # o = Expense(**d)
            # o.save()
            o = form.save()
            # TODO: show success message
            return redirect(o)
            # return redirect("expenses:list")
    else:
        form = forms.ExpenseForm()

    return render(
        request,
        "expenses/expense_form.html",
        {
            "form": form,
        },
    )

