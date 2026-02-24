from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from services.expense_service import (
    create_expense,
    get_user_expenses,
    get_total_expenses,
)
from .models import Expense
from .forms import ExpenseForm


@login_required
def expense_list_view(request):
    expenses = get_user_expenses(request.user)
    total = get_total_expenses(request.user)

    return render(
        request,
        "expenses/expense_list.html",
        {"expenses": expenses, "total": total},
    )


@login_required
def expense_create_view(request):
    form = ExpenseForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        create_expense(request.user, form.cleaned_data)
        return redirect("expense_list")

    return render(request, "expenses/expense_form.html", {"form": form})