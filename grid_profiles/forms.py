from django.forms import ModelForm
from grid_user.models import User
from grid_profiles.models import Userprofile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit#, Layout, Div,  HTML, Button, Row, Field

class UserProfileForm(ModelForm):
	"""docstring for ProfileForm"""

	class Meta:
		model = Userprofile
		fields = ['homepage', 'displayname', 'profileimage', 'profileabouttext',
		'profilefirstimage', 'profilefirsttext' ]

	def __init__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_id = 'add-article'
		self.helper.form_class = 'form-horizontal'
		#self.helper.label_class = 'col-sm-2'
		self.helper.layout.append(Submit('save', 'save'))
			