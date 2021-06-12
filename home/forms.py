from django import forms
from accounts.models import User

class UsersettingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['readonly'] = 'readonly'
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'nickname', 'email')
