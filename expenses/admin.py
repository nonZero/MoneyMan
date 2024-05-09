from django.contrib import admin

from expenses.models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "amount",
        "date",
    ]

    search_fields = [
        "id",
        "title",
        "amount",
        "date",
    ]

    date_hierarchy = "date"
