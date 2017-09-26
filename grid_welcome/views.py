from django.shortcuts import render_to_response, render
from django.http import HttpResponse
import sys, os

def Welcome(request):

  # This will come from search
  locations = [
    {'name':'BlueWall','slurl':'BlueWall','text':'Red\'s BBQ & Bait Shop'},
    {'name':'OGP Island','slurl':'BlueWall Isle','text':'Lindens have been here'},
    {'name':'Gateway','slurl':'BlueWall Gateway','text':'Hypergrid Access to OSGrid'},
    {'name':'Sandbox','slurl':'Sloodleville','text':'BlueWall\'s sandbox region'},
    {'name':'Test Lab','slurl':'BlueWall X10','text':'Advanced projects lab - You can rez here, but I\'ll have to shoot chya'}]

  event_list = [{'name':'Blues Concert','location':'BlueWall'},{'name':'Scripting Class','location':'Sloodleville'}
  ]

  return render(request,'welcome.html', {'rezpoints': locations, 'events': event_list,'welcome_title' : 'Welcome Title' , 'welcome_heading' : 'Welcome heading'})

