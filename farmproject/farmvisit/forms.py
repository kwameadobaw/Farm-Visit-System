from django import forms
from .models import FarmVisit

class FarmVisitForm(forms.ModelForm):
    # Custom fields for multiple checkboxes
    crop_issues_choices = [
        ('Pests', 'Pests'),
        ('Diseases', 'Diseases'),
        ('Nutrient Deficiency', 'Nutrient Deficiency'),
        ('Poor Germination', 'Poor Germination'),
        ('Water Stress', 'Water Stress'),
    ]
    
    livestock_issues_choices = [
        ('Illness', 'Illness'),
        ('Parasites', 'Parasites'),
        ('Malnutrition', 'Malnutrition'),
        ('Poor Housing', 'Poor Housing'),
    ]
    
    # Create MultipleChoiceField for checkboxes
    crop_issues_list = forms.MultipleChoiceField(
        choices=crop_issues_choices,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    livestock_issues_list = forms.MultipleChoiceField(
        choices=livestock_issues_choices,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    class Meta:
        model = FarmVisit
        fields = '__all__'
        exclude = ['crop_issues', 'livestock_issues', 'created_at', 'updated_at']
        widgets = {
            'visit_date': forms.DateInput(attrs={'type': 'date'}),
            'follow_up_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # If we're editing an existing instance, populate the checkbox fields
        if self.instance.pk:
            if self.instance.crop_issues:
                self.initial['crop_issues_list'] = self.instance.crop_issues.split(',')
            if self.instance.livestock_issues:
                self.initial['livestock_issues_list'] = self.instance.livestock_issues.split(',')
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Convert checkbox lists to comma-separated strings
        instance.crop_issues = ','.join(self.cleaned_data.get('crop_issues_list', []))
        instance.livestock_issues = ','.join(self.cleaned_data.get('livestock_issues_list', []))
        
        if commit:
            instance.save()
        return instance