from django.shortcuts import render_to_response, render
from grid_profiles.forms import UserProfileForm
from grid_profiles.models import Userprofile
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
	context = {}
	user = authenticate(email='abc@abc.com', password='12345')
	user_profile = user 
	userprofileobj, crt = Userprofile.objects.get_or_create(user=user_profile)
	if request.method=='POST':
		form = UserProfileForm(request.POST, request.FILES, instance=userprofileobj)
		if form.is_valid():
			up = form.save(commit=False)
			up.user = user_profile
			up.save()

			return HttpResponseRedirect('/')
		else:
			form.errors
	else:
		form = UserProfileForm(instance=userprofileobj)
	context['form'] = form
	return render(request, "profile.html", context)
  

