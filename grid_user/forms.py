from django import forms
from django.forms.models import ModelForm
from crispy_forms.layout import (
    Submit, Layout, Fieldset, ButtonHolder, HTML, MultiField, Div)
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from grid_user.models import SECURTYQUESTION, TempUser
from parsley.decorators import parsleyfy

class UserAccessForm(forms.Form):

    email = forms.CharField(
        label="Email",
        max_length=98,
        required=True,
    )

    password = forms.CharField(
        label='Password',
        max_length=18,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'auth_user_form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = '/login/'

        self.helper.add_input(Submit('submit', 'Login'))
        super(UserAccessForm, self).__init__(*args, **kwargs)

@parsleyfy
class CreateUserForm(ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput, required=True
        )
    username = forms.CharField(required=True)

    helper = FormHelper()
    # helper.form_id = 'registration-form'
    # helper.form_class = 'form-horizontal'
    helper.form_tag = False
    # helper.form_action = '.'
    helper.layout = Layout(
            Div(
                Div('username', css_class='page-row-right'),
                Div('email', css_class='page-row-right'),
                Div('firstname', css_class='page-row-right'),
                Div('lastname', css_class='page-row-right'),
                Div('dob', css_class='page-row-right'),
                Div('password', css_class='page-row-right'),
                Div('securtyq', css_class='page-row-right'),
                Div('securtya', css_class='page-row-right'),
                css_class='page-row'
            ),
    )
    helper.layout.append(
        FormActions(
            Submit('save', 'Create Account')
        )
    )

    class Meta:
        model = TempUser
        exclude = ("activation_key", "created")

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['dob'].label = "Date of Birth"
        self.fields['securtyq'].label = "Security Question"
        self.fields['securtya'].label = "Security Answer"
