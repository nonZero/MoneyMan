from django import forms

from . import models
from .models import Category


class SearchInput(forms.TextInput):
    input_type = "search"


class SearchForm(forms.Form):
    q = forms.CharField(required=False, label="", widget=SearchInput)
    category = forms.ModelChoiceField(Category.objects.all(), required=False)
    recent_only = forms.BooleanField(required=False, label="Only from the last 90 days")
    sort_field = forms.ChoiceField(choices=[('date', 'Date'), ('amount', 'Price')])


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


