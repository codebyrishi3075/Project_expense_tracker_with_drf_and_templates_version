from rest_framework import viewsets, permissions
from services.budget_service import get_user_budgets, create_budget
from apps.budgets.models import Budget
from .serializers import BudgetSerializer


class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return get_user_budgets(self.request.user)

    def perform_create(self, serializer):
        create_budget(self.request.user, serializer.validated_data)