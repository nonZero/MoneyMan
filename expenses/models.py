from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=500, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def first_letter(self):
        return self.name[0]


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='expenses')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='expenses')
    title = models.CharField(max_length=500)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"[#{self.id}] {self.amount} @ {self.date} {self.title}"

    def get_absolute_url(self):
        return reverse("expenses:detail", args=(self.id,))

    def is_expensive(self):
        return self.amount > 25
