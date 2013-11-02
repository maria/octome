from django.http import HttpResponse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        html = "<h1> Buna! </h1>"
        return HttpResponse(html)
