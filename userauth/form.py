from django import forms
from userauth.models import UserProfile



class userProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture')