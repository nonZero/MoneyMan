from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from expenses.models import Expense
from expenses.serializers import ExpenseSerializer


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ListExpenses(APIView):
    def get(self, request, format=None):
        qs = Expense.objects.filter(user=self.request.user)
        data = {
            "items": ExpenseSerializer(instance=qs, many=True).data,
        }
        return Response(data)
