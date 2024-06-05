import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

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


class ExpenseCreateView(ExpenseMixin, SuccessMessageMixin, CreateView):
    form_class = forms.ExpenseForm
    success_message = "Expense '%(title)s' created."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseUpdateView(ExpenseMixin, SuccessMessageMixin, UpdateView):
    form_class = forms.ExpenseForm
    success_message = "Expense '%(title)s' updated."


class ExpenseDeleteView(ExpenseMixin, SuccessMessageMixin, DeleteView):
    success_url = reverse_lazy("expenses:list")

    def get_success_message(self, cleaned_data):
        return f"Expense #{self.kwargs['pk']} deleted."


# @login_required
# def expense_create(request: HttpRequest):
#     if request.method == "POST":
#         form = forms.ExpenseForm(request.POST)
#         if form.is_valid():
#             form.instance.user = request.user
#             o = form.save()
#             messages.success(request, f"Expense #{o.id} created.")
#             return redirect(o)
#     else:
#         form = forms.ExpenseForm()
#
#     return render(
#         request,
#         "expenses/expense_form.html",
#         {
#             "form": form,
#         },
#     )
