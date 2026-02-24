from django.db.models import Sum
from apps.budgets.models import Budget
from apps.expense.models import Expense


def create_budget(user, data):
    return Budget.objects.create(user=user, **data)


def update_budget(budget, data):
    for attr, value in data.items():
        setattr(budget, attr, value)
    budget.save()
    return budget


def delete_budget(budget):
    budget.delete()


def get_user_budgets(user):
    return Budget.objects.filter(user=user)


def get_budget_total_spent(budget):
    total = (
        Expense.objects
        .filter(
            user=budget.user,
            budget=budget,
            date__range=(budget.start_date, budget.end_date)
        )
        .aggregate(total=Sum("amount"))
        .get("total")
    )
    return total or 0


def get_budget_remaining(budget):
    spent = get_budget_total_spent(budget)
    return budget.amount_limit - spent