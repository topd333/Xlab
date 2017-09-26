from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import sys, os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from django.core.exceptions import ObjectDoesNotExist


from models import AuthList

import logging

log = logging.getLogger("[AUTHORIZATION]:")

@csrf_exempt
def authorize(request):

  log.info('Authorize Start')

  data = request.body
  xdoc = ET.fromstring(data)

  region = xdoc.find('RegionID').text
  user = xdoc.find('ID').text

  mssg = 'not authorized'
  auth = 'false'
  try:
    xauth = AuthList.objects.get(user_id=user,region_id=region)
    xfields = (xauth.user_name, xauth.region_name)
    if xauth.user_id == user and xauth.region_id == region:
      auth = 'true'
      mssg = '%s is authroized on %s'%xfields
    else:
      auth = 'false'
  except ObjectDoesNotExist:
    pass

  top = Element('AuthorizationResponse')
  child = SubElement(top,'IsAuthorized')
  child.text = auth
  message = SubElement(top, 'Message')
  message.text = mssg

  resp_text = '<?xml version="1.0"?>%s'%tostring(top)
  return HttpResponse(resp_text,content_type="text/xml")


