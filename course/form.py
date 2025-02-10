from django import forms
from .models import Course, ExcelFile
    
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'duration', 'desc', 'fee')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'fee': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Course.objects.filter(name=name).exists():
            raise forms.ValidationError(
                'A course with this name already exists'
            )
        return name
    
class FileForm(forms.ModelForm):
    class Meta:
        model = ExcelFile
        fields = ('file',)
        widgets = {
            'file' : forms.FileInput(attrs={'class':'form-control'})
        }