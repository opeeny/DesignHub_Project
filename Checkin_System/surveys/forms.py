from django import forms
class LoginForm(forms.Form):
    user = forms.CharField(label = 'Username', max_length = 100)
    password = forms.CharField(max_length = 32, widget = forms.PasswordInput, label = "Password")

class SearchForm(forms.Form):
    visitor_name = forms.CharField(label="Search", max_length = 100)
class AddForm(forms.Form):
    name = forms.CharField(label = 'Full name', max_length = 100)
    company = forms.CharField(label = "Company's name", max_length = 100)
    temperature = forms.IntegerField(max_value = 50)
    id_number = forms.CharField(label = 'ID number', max_length = 100)
    telephone_number = forms.CharField(label = 'Phone number', max_length = 100)
    date = forms.DateField(label = 'Date', widget = forms.DateInput)
class EditVisitorForm(forms.Form):
    date = forms.DateField(label = 'Date', widget = forms.DateInput)
    temperature = forms.IntegerField(max_value = 50)