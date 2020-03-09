from django.contrib.auth import get_user_model
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from index.models import EmailAddress
from django.utils.translation import gettext as _


def validate_hris_id_exists(value):
    hris_id = EmailAddress.objects.filter(pk=value)
    if not hris_id:  # check if any object exists
        raise ValidationError('HRIS ID does not exist')


class SignupForm(forms.ModelForm):
    use_required_attribute = False

    numeric = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed')
    hris_id = forms.CharField(max_length=5, label='HRIS ID', validators=[numeric, validate_hris_id_exists],
                              widget=forms.TextInput({'placeholder': 'HRIS ID'}))

    class Meta:
        model = get_user_model()
        fields = ['hris_id']

    def clean(self):
        hris_id = self.cleaned_data.get("hris_id")
        email_input = self.cleaned_data.get("email")
        if hris_id:
            validate_email = EmailAddress.objects.get(pk=hris_id)  # Query using get pk=hris_id
            if not validate_email.email_address == email_input:  # compare query to email variable
                self.add_error('email',
                               _("Email does not match the inputted HRIS ID"))  # if not match, then raise error

        return self.cleaned_data

    def signup(self, request, user):
        user.hris_id = self.cleaned_data['hris_id']
        user.save()
