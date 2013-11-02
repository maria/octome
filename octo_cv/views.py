from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)
