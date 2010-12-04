from django import forms
from django.contrib.auth.models import User

''' Borrowing code from ubernostrom's django-registration app. '''
class NewUserForm(forms.Form):
    ''' Form from creating a new user '''
    username = forms.RegexField(regex=r'^\w+$',
                                max_length=30,
                                widget = forms.TextInput(),
                                label = 'Username',
                                error_messages={'invalid': "This value may only contain letters, numbers, and underscores."})
    email = forms.EmailField(label='Email', max_length='30')
    password1 = forms.CharField(widget = forms.PasswordInput(render_value=False),
                                label = "Password")
    password2 = forms.CharField(widget = forms.PasswordInput(render_value=False),
                                label = "Password (again)")

    def clean_username(self):
        '''
        Make sure the username isn't already in use and it's alphanumeric.
        '''
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("This username is already in use.")

        def clean(self):
            ''' Make sure the passwords match '''
            if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
                if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                    raise forms.ValidationError("Passwords don't match.")
            return self.cleaned_data
