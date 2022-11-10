from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class CreationForm(UserCreationForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'})) 
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'dob')
        widgets = {
            'dob': forms.DateInput(attrs={'class': 'datepicker'}),
               }
