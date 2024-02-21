from django import forms
from accounts.models import customer,vendor

class vendorform(forms.ModelForm):
    class Meta:
        model=vendor
        fields="__all__"

class customerform(forms.ModelForm):
    class Meta:
        model=customer
        fields="__all__"
