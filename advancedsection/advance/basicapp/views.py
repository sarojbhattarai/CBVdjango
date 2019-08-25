from django.views.generic import View, TemplateView
from django.shortcuts import render
#from django.http import HttpResponse



'''def index(request):
    return render (request, 'basicapp/index.html')

class ClassBasedView(View):
    def get(self, request):
        return HttpResponse("Hello World!")
'''

class Index(TemplateView):
    template_name = 'basicapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context