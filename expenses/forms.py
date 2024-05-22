from django import forms

from . import models
from .models import Category


class SearchInput(forms.TextInput):
    input_type = "search"


class SearchForm(forms.Form):
    q = forms.CharField(required=False, label="", widget=SearchInput)
    recent_only = forms.BooleanField(required=False)
    minimum_price = forms.IntegerField(initial=10, required=False)
    sort_field = forms.ChoiceField(choices=[('date', 'Date'), ('amount', 'Price')])
    category = forms.ModelChoiceField(Category.objects.all(), required=False)


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = models.Expense
        fields = (
            'category',
            'amount',
            'title',
            'date',
            'description',
        )


