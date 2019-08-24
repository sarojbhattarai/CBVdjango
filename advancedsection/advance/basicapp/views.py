from django.views.generic import View
from django.http import HttpResponse



'''def index(request):
    return render (request, 'basicapp/index.html')
'''
class ClassBasedView(View):
    def get(self, request):
        return HttpResponse("Hello World!")
