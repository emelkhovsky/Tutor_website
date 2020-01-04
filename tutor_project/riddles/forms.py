from django import forms

class email_form(forms.Form):
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Ваш email или номер телефона', 'id': 'input_con'}))