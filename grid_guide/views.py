from django.shortcuts import render_to_response, render
from django.http import HttpResponse
import sys, os

# Create your views here.


def Guide(request):

  locations = [
  {'name':'Linkedinyou','slurl':'Linkedinyou','text':'Red\'s BBQ & Bait Shop'},
  {'name':'OGP Island','slurl':'Linkedinyou Isle','text':'Lindens have been here'},
  {'name':'Gateway','slurl':'Linkedinyou Gateway','text':'Hypergrid Access to OSGrid'},
  {'name':'Sandbox','slurl':'Sloodleville','text':'Linkedinyou\'s sandbox region'},
  {'name':'Test Lab','slurl':'Linkedinyou X10','text':'Advanced projects lab - You can rez here, but I\'ll have to shoot chya'}]

  return render(request,'guide.html', {'rezpoints': locations, })

