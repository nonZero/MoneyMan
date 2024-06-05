import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from . import forms
from .models import Expense


# class View:
#     @classmethod
#     def as_view(cls, **cls_kwargs):
#         def view(request: HttpRequest, *args, **kwargs):
#             o = cls()
#             for k, v in cls_kwargs.items():
#                 setattr(o, k, v)
#             return o.dispatch(request, *args, **kwargs)
#         return view
#
#     def dispatch(self, request, *args, **kwargs):
#         self.request = request
#         m = request.method.lower()
#         func = getattr(self, m)
#         return func(request, *args, **kwargs)
#
#
# class TemplateView(View):
#     def get(self, request):
#         context = self.get_context_data()
#         return render(request, self.template_name, context)
#
#     def get_context_data(self):
#         return {
#             'request': self.request,
#         }
#
# class AddUserToContextData:
#     def get_context_data(self):
#         d = super().get_context_data()
#         d['user'] = self.request.user
#         return d
#
#
# class MyView1(TemplateView):
#     template_name = "my.html"
#
#     def get_context_data(self):
#         d = super().get_context_data()
#         d['foo'] = 1
#         return d
#
#
# class MyView2(View):
#     def dispatch(self, request):
#         print(self.x)
#     ...


class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
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

        return qs.filter(user=self.request.user)


# @login_required
# def expense_list(request: HttpRequest):
#     qs = Expense.objects.order_by("-date")
#     qs = qs.filter(user=request.user)
#
#     form = forms.SearchForm(request.GET if request.GET else None)
#
#     if form.is_valid():
#         d = form.cleaned_data
#         if d['q']:
#             qs = qs.filter(title__icontains=d['q'])
#         if d['recent_only']:
#             day = datetime.date.today() - datetime.timedelta(days=90)
#             qs = qs.filter(date__gte=day)
#         if d['category']:
#             qs = qs.filter(category=d['category'])
#         qs = qs.order_by("-" + d['sort_field'])
#         # the next two lines disables displaying the form validation css classes.
#         form.initial = form.cleaned_data
#         form.is_bound = False
#
#     return render(
#         request,
#         "expenses/expense_list.html",
#         {
#             "object_list": qs[:20],
#             "form": form,
#         },
#     )


@login_required
def expense_detail(request: HttpRequest, id: int):
    return render(
        request,
        "expenses/expense_detail.html",
        {
            "object": get_object_or_404(Expense, id=id, user=request.user),
        },
    )


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
