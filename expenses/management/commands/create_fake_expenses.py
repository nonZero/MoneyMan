import tqdm
from django.core.management.base import BaseCommand
from faker import Faker
import random
from expenses.models import Expense


class Command(BaseCommand):
    help = "Create fake expenses"

    def add_arguments(self, parser):
        parser.add_argument("n", type=int)

    def handle(self, n, *args, **options):
        faker = Faker()
        for i in tqdm.tqdm(range(n)):
            Expense.objects.create(
                title=faker.sentence(),
                amount=str(random.randint(100, 10000) / 100),
                date=faker.date_this_decade(),
            )
