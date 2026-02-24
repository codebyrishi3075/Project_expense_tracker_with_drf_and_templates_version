from django.db import models
from django.conf import settings


class Expense(models.Model):
    CATEGORY_CHOICES = (
        ("FOOD", "Food"),
        ("TRAVEL", "Travel"),
        ("BILLS", "Bills"),
        ("SHOPPING", "Shopping"),
        ("OTHER", "Other"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="expenses"
    )
    budget = models.ForeignKey(
    "budgets.Budget",
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="expenses"
    )
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField()
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]
        indexes = [
            models.Index(fields=["user", "date"]),
            models.Index(fields=["category"]),
        ]

    def __str__(self):
        return f"{self.title} - {self.amount}"