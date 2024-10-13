from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Register

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'date_of_birth',
            'gender',
            'location',
            'primary_bank',
            'investment_accounts',
            'retirement_accounts',
            'investment_goals',
            'debt_types',
            'debt_amounts',
            'interest_rates',
            'debt_repayment_plans',
            'income_sources',
            'income_amount',
            'expense_categories',
            'expense_amounts',
            'insurance_types',
            'insurance_coverage',
            'insurance_premiums',
            'short_term_goals',
            'long_term_goals',
        )