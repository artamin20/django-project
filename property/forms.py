from django import forms
from django.db.models import fields
from .models import Reserve


class ReserveFrom(forms.ModelForm):
    class Meta :
        model = Reserve
        fields = '__all__'