from django.views.generic.simple import direct_to_template


from django import http
from django.conf import settings

def home(request):
    return direct_to_template(request,'home.html')

