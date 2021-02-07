from django import forms
from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'