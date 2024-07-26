from django.forms import PasswordInput, CharField, Form


class UserForm(Form):
    username = CharField(max_length=150)
    password = CharField(widget=PasswordInput)
