import random
import string
from django import forms
from .models import StudentRegistration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = ['name', 'college_name', 'year_of_study', 'phone_number', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'college_name': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def generate_azeoid(self):
        # Take first 3 letters of name (upper case) and year of study
        name_part = self.cleaned_data['name'][:3].upper()
        year_part = self.cleaned_data['year_of_study']
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        return f"AZEO-{name_part}{year_part}-{random_part}"

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.azeoid:
            while True:
                new_id = self.generate_azeoid()
                if not StudentRegistration.objects.filter(azeoid=new_id).exists():
                    instance.azeoid = new_id
                    break
        if commit:
            instance.save()
        return instance