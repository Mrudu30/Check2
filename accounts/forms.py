from django import forms
from .models import course, Student,Parents,Exam

class studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('username','first_name','last_name','ph_no','email','password','course')
        
class edit_details(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username','first_name','last_name','password','ph_no','course','date_joined','leaving_date']
        widgets = {
            'password':forms.PasswordInput()
        }  
        
class parentform(forms.ModelForm):
    class Meta:
        model = Parents  
        fields = '__all__' 
        widgets = {
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'guardian_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mail1': forms.EmailInput(attrs={'class': 'form-control'}),
            'mail2': forms.EmailInput(attrs={'class': 'form-control'}),
            'ph1': forms.NumberInput(attrs={'class': 'form-control'}),
            'ph2': forms.NumberInput(attrs={'class': 'form-control'}),
        }       