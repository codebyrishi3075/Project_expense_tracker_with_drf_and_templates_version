from rest_framework import viewsets, permissions
from services.expense_service import get_user_expenses, create_expense
from apps.expense.models import Expense
from .serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return get_user_expenses(self.request.user)

    def perform_create(self, serializer):
        create_expense(self.request.user, serializer.validated_data)