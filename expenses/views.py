import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from . import forms
from .models import Expense


class ExpenseMixin(LoginRequiredMixin):
    model = Expense
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ExpenseListView(ExpenseMixin, ListView):
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()

        form = forms.SearchForm(self.request.GET if self.request.GET else None)

        if form.is_valid():
            d = form.cleaned_data
            if d['q']:
                qs = qs.filter(title__icontains=d['q'])
            if d['recent_only']:
                day = datetime.date.today() - datetime.timedelta(days=90)
                qs = qs.filter(date__gte=day)
            if d['category']:
                qs = qs.filter(category=d['category'])
            qs = qs.order_by("-" + d['sort_field'])
            # the next two lines disables displaying the form validation css classes.
            form.initial = form.cleaned_data
            form.is_bound = False

        self.form = form

        return qs


class ExpenseDetailView(ExpenseMixin, DetailView):
    pass


@login_required
def expense_create(request: HttpRequest):
    if request.method == "POST":
        form = forms.ExpenseForm(request.POST)
        if form.is_valid():
            # d = form.cleaned_data
            # o = Expense(**d)
            # o.save()
            form.instance.user = request.user
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
