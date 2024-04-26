from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'attached_file']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),  
        }
