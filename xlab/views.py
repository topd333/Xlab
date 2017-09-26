
from django.shortcuts import render_to_response, render
from django.template import loader, RequestContext
from django.http import HttpResponse
import random
import models
from django.conf import settings

def home(request):
  
  context = {}
  context['SiteName'] = settings.SITE_NAME
  context['page_title'] = '%s: Welcome'%(settings.SITE_NAME)

  context['img'] = random.randint(0,7)
  context['navbar'] = 'site_nav.html'
  context['form_action'] = '/login/'
  context['show_language'] = True;
  
  return render(request, "index.html", context)

