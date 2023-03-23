from django import forms
from datetime import date
from django.forms import ModelForm
from .models import post



class UserModelForm(ModelForm):
    current_date = date.today()
    YEARS = [x for x in range(current_date.year - 1, current_date.year + 6)]
    today = current_date.strftime("%Y-%m-%d")

    date_added = forms.DateField(initial=today, widget=forms.SelectDateWidget(years=YEARS))

    class Meta:
        model = post
        fields = ['id_number', 'loan_name', 'loan_amount', 'loan_interest', 'loan_duration']