from rest_framework import serializers

from expenses import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    # url = serializers.URLField(target="self")
    # category = CategorySerializer()
    # really_expensive = serializers.BooleanField(source='is_expensive')
    # foo = serializers.SerializerMethodField()
    # name = serializers.CharField(source='title')

    class Meta:
        model = models.Expense
        fields = [
            "id",
            "url",
            "user",
            "category",
            "title",
            "amount",
            "date",
            "description",
            "is_star",
        ]

    def get_foo(self, instance):
        return "!!!"


print(ExpenseSerializer())


class ShortExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expense
        fields = [
            "title",
            "amount",
        ]

    def get_foo(self, instance):
        return "!!!"
