from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from octo_cv.models import Contact
from octo_cv.constants import ContactType


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get(self, request):
        """Get all the Contacts of type Social Profile and create a mapping:
            social_contact_name -> social_contact_object,
        to display them in a given order in the view.
        """
        view_social_contacts = dict()
        social_contacts = Contact.objects.filter(type=ContactType.SOCIAL)

        for social_contact in social_contacts:
            view_social_contacts[social_contact.name.lower()] = social_contact
        return render(request, self.template_name,
                      {'social_contacts': view_social_contacts})


class WorkView(TemplateView):
    template_name = 'work.html'

    def get(self, request):
        return render(request, self.template_name)


class EducationView(TemplateView):
    template_name = 'education.html'

    def get(self, request):
        return render(request, self.template_name)


class VolunteerView(TemplateView):
    template_name = 'volunteer.html'

    def get(self, request):
        return render(request, self.template_name)


class AboutView(TemplateView):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name)
