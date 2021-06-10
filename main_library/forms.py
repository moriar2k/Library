from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    last_name = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    mobile = forms.IntegerField(required=False, label=u'komórka')
    # is it valid to put the here??
    last_login = datetime.datetime.now()
    date_joined = datetime.datetime.now()

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
