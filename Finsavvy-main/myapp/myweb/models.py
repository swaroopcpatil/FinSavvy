# from django.db import models
# from django.contrib.auth.models import User

# class Register(models.Model):
#     # Personal Information
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=20)
#     date_of_birth = models.DateField()
#     gender = models.CharField(max_length=10)
#     location = models.CharField(max_length=255)

#     # Financial Information
#     primary_bank = models.CharField(max_length=255)
#     investment_accounts = models.TextField()
#     retirement_accounts = models.TextField()
#     investment_goals = models.TextField()

#     # Debt Information
#     debt_types = models.TextField()
#     debt_amounts = models.TextField()
#     interest_rates = models.TextField()
#     debt_repayment_plans = models.TextField()

#     # Income and Expenses
#     income_sources = models.TextField()
#     income_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     expense_categories = models.TextField()
#     expense_amounts = models.TextField()  # Corrected indentation

#     # Insurance Information
#     insurance_types = models.TextField()
#     insurance_coverage = models.TextField()
#     insurance_premiums = models.TextField()

#     # Financial Goals
#     short_term_goals = models.TextField()
#     long_term_goals = models.TextField()

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

from django.contrib.auth.models import User
from django.db import models

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Temporarily allow null
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()  # Optional, can be removed since User model has email
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=200)
    primary_bank = models.CharField(max_length=200)
    investment_accounts = models.TextField()
    retirement_accounts = models.TextField()
    investment_goals = models.TextField()
    debt_types = models.TextField()
    debt_amounts = models.TextField()
    interest_rates = models.TextField()
    debt_repayment_plans = models.TextField()
    income_sources = models.TextField()
    income_amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_categories = models.TextField()
    expense_amounts = models.TextField()
    insurance_types = models.TextField()
    insurance_coverage = models.TextField()
    insurance_premiums = models.TextField()
    short_term_goals = models.TextField()
    long_term_goals = models.TextField()
