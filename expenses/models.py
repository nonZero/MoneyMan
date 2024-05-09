from django.db import models


# ORM: Object Relational Mapper


class Expense(models.Model):
    title = models.CharField(max_length=500)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"[#{self.id}] {self.amount} @ {self.date} {self.title}"

    def is_expensive(self):
        return self.amount > 25
