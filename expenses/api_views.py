from django.db.models import Sum, Max, Min, Count
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from expenses.models import Expense, Category
from expenses.serializers import ExpenseSerializer


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    @action(detail=False)
    def total(self, request):
        # qs = self.get_queryset()
        # SELECT SUM(amount) from expenses_expense;
        info = Expense.objects.aggregate(
            count=Count("*"),
            sum=Sum("amount"),
            max=Max("amount"),
            min=Min("amount"),
        )
        return Response(info)

    @action(detail=False, url_path="per-category")
    def per_category(self, request):
        qs = Category.objects.annotate(total=Sum("expenses__amount"))
        # TODO: CategorySerializer
        return Response(
            {
                "id": c.id,
                "name": c.name,
                "total": c.total,
            }
            for c in qs
        )

    @action(detail=True)
    def expensive(self, request, pk: int):
        o = self.get_object()
        return Response(
            {
                "expensive": o.is_expensive(),
            }
        )


class ListExpenses(APIView):
    def get(self, request, format=None):
        qs = Expense.objects.filter(user=self.request.user)
        data = {
            "items": ExpenseSerializer(instance=qs, many=True).data,
        }
        return Response(data)
