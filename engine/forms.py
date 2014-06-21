from django import forms


class EventCreateForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))

class GuestSignInForm(forms.Form):
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))


