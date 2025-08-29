from django import forms
from .models import PrescriptionUpload
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = PrescriptionUpload
        fields = ['name','phone','notes','file']
