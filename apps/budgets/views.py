from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from services.budget_service import (
    create_budget,
    get_user_budgets,
    get_budget_total_spent,
    get_budget_remaining,
)
from .models import Budget
from .forms import BudgetForm


@login_required
def budget_list_view(request):
    budgets = get_user_budgets(request.user)

    budget_data = []
    for budget in budgets:
        budget_data.append({
            "budget": budget,
            "spent": get_budget_total_spent(budget),
            "remaining": get_budget_remaining(budget),
        })

    return render(
        request,
        "budgets/budget_list.html",
        {"budget_data": budget_data},
    )


@login_required
def budget_create_view(request):
    form = BudgetForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        create_budget(request.user, form.cleaned_data)
        return redirect("budget_list")

    return render(request, "budgets/budget_form.html", {"form": form})