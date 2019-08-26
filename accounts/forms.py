from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import userProfile,Employee


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username','first_name','last_name' ,'email', 'password1', 'password2')
    def password_match(self,*args,**kwargs):
        password1= self.cleaned_data.get('password1')
        password2= self.cleaned_data.get('password2')
        if password1 is not password2: 
            raise forms.ValidationError("Passwords do not match")
        else:
            return password1
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password1'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password2'].widget.attrs.update({'class' : 'form-control'})




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ('profile_pic','can_upload')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['can_upload'].widget.attrs.update({'class' : 'form-control'})
        self.fields['can_upload'].label = 'Do you want to upload content'
        
class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('number','occupation','profile_pic')
    def __init__(self, *args, **kwargs):
        super(EmployeeCreateForm, self).__init__(*args, **kwargs)
        self.fields['occupation'].widget.attrs.update({'class' : 'form-control'})
        self.fields['number'].widget.attrs.update({'class' : 'form-control'})
