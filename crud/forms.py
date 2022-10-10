from dataclasses import fields
from socket import fromshare
from django import forms
from .models import employee


class emp(forms.ModelForm):
    class Meta:
        model = employee
        fields = "__all__"
