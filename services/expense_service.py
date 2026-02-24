from django.db.models import Sum
from apps.expense.models import Expense


def create_expense(user, data):
    return Expense.objects.create(user=user, **data)


def update_expense(expense, data):
    for attr, value in data.items():
        setattr(expense, attr, value)
    expense.save()
    return expense


def delete_expense(expense):
    expense.delete()


def get_user_expenses(user):
    return Expense.objects.filter(user=user)


def get_total_expenses(user):
    total = (
        Expense.objects
        .filter(user=user)
        .aggregate(total=Sum("amount"))
        .get("total")
    )
    return total or 0