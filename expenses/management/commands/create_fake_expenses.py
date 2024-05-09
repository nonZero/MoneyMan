import tqdm
from django.core.management.base import BaseCommand
from faker import Faker
import random
from expenses.models import Expense


class Command(BaseCommand):
    help = "Create fake expenses"

    def add_arguments(self, parser):
        parser.add_argument("n", type=int)
        parser.add_argument("--delete", action="store_true")

    def handle(self, n, delete, *args, **options):
        if delete:
            Expense.objects.all().delete()

        faker = Faker()
        for i in tqdm.tqdm(range(n)):
            Expense.objects.create(
                title=faker.sentence(),
                amount=str(random.randint(100, 10000) / 100),
                date=faker.date_this_decade(),
                description="\n".join(
                    faker.paragraph() for i in range(random.randint(2, 5))
                ),
            )
