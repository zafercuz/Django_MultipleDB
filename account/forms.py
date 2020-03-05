from django.contrib.auth import get_user_model
from django import forms
from django.core.validators import RegexValidator


class SignupForm(forms.ModelForm):
    use_required_attribute = False

    numeric = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed')
    hris_id = forms.CharField(max_length=5, label='HRIS ID', validators=[numeric], widget=forms.TextInput({
        'placeholder': 'HRIS ID'
    }))

    class Meta:
        model = get_user_model()
        fields = ['hris_id']

    def signup(self, request, user):
        user.hris_id = self.cleaned_data['hris_id']
        user.save()
