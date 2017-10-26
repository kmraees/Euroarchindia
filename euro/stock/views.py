from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from django.views.generic.base import TemplateView
from stock.models import products

def hello(request):
  name="scgvds"
  html="<html><body>hi %s. dsdewedw</body></html>" % name
  return HttpResponse(html)
  
def product(request):
 entries= products.objects.all()
  
 return render_to_response('product.html',{'products' : entries},context_instance=RequestContext(request))

def home(request):
 return render_to_response('euro.html')
 
def about(request):
  return render_to_response('about.html')
  
def contact(request):
  return render_to_response('contact.html')