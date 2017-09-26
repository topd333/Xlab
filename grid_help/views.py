from django.shortcuts import render_to_response, render
from django.http import HttpResponse
import sys, os

def Help(request):

  # This will come from search

  return HttpResponse('Help is on the way')

def About(request):

  # This will come from search

  return HttpResponse('Xlab is brought to you by Linkedinyou Information Technmologies, LLC in Liberty, South Carolina')

