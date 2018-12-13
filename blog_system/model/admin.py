# coding=utf8
from django.contrib import admin
from django import forms
from model.models import User

class UserCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        placeholder = {'user_name':'用户名', 'email':'邮箱',
                'password1':'密码','password2':'密码确认'}
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'placeholder':placeholder[field]
                })

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('user_name','email')
 
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
 
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
# Register your models here.
