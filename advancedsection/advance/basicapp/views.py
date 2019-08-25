from django.views.generic import View, TemplateView, ListView, DetailView
from django.shortcuts import render
from . import models
#from django.http import HttpResponse



###
#def index(request):
#   return render (request, 'basicapp/index.html')

#class ClassBasedView(View):
#    def get(self, request):
#       return HttpResponse("Hello World!")
#'''
#This is second commit 
#'''

#class Index(TemplateView):
#    template_name = 'basicapp/index.html'
#
#    def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'BASIC INJECTION!'
#         return context
#'''

class Index(TemplateView):
    template_name = 'basicapp/index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'basicapp/school_detail.html'
