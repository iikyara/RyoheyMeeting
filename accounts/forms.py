from accounts.models import User
from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['nickname'].widget.attrs['class'] = 'form-control'


    class Meta:
       model = User
       fields = ("username", "password1", "password2", "nickname",)