from django import forms

from django.contrib.auth.models import User


class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
   

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    #validate pwd
    def clean_pwd(self):
	cd = self.cleaned_data
	if cd['pasword1'] != cd['password2']:
		raise ValidationError("Pwd doesn't match")
	return c['password1']
