import tqdm
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from faker import Faker
import random
from expenses.models import Expense, Category

CATS = [
    'Food',
    'House',
    'Fun',
    'Taxes',
    'Car',
]


class Command(BaseCommand):
    help = "Create fake expenses"

    def add_arguments(self, parser):
        parser.add_argument("n", type=int)
        parser.add_argument("--delete", action="store_true")

    def handle(self, n, delete, *args, **options):
        if delete:
            Expense.objects.all().delete()

        faker = Faker()

        def cu(name):
            try:
                return User.objects.create_user(username=name, password="secret")
            except IntegrityError:
                return User.objects.get(username=name)

        users = [
            cu(f"user{i}") for i in range(5)
        ]

        cats = [
            Category.objects.get_or_create(name=c)[0] for c in CATS
        ]

        for i in tqdm.tqdm(range(n)):
            Expense.objects.create(
                user=random.choice(users),
                category=random.choice(cats),
                title=faker.sentence(),
                amount=str(random.randint(100, 10000) / 100),
                date=faker.date_this_decade(),
                description="\n".join(
                    faker.paragraph() for i in range(random.randint(2, 5))
                ),
            )
