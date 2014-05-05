from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from octo_cv.models import Contact, Education, Work, Project
from octo_cv.constants import ContactType, WorkType


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get(self, request):
        """Get all the Contacts ordered by type and name, and then we separate
        them based on their network type, in order to display them in a given
        order in the view.
        Hence the GitHub & Linkedin aka Professional networks are displayed
        between the General information profile and social profiles.
        Construct a general contact object to display contact information like
        emailself.
        """
        contacts = Contact.objects.filter(type__in=[ContactType.SOCIAL,
            ContactType.ADDRESS]).order_by('type').order_by('name')

        general_contacts = Contact.objects.filter(network='General')

        general_contact = Contact()
        for contact in general_contacts:
            setattr(general_contact, contact.type.lower(), contact.description)

        template_data = {
            'professional_networks': contacts.filter(network='Professional'),
            'social_networks': contacts.filter(network='Social'),
            'general_contact': general_contact}

        return render(request, self.template_name, template_data)


class WorkView(TemplateView):
    template_name = 'work.html'

    def get(self, request):
        works = Work.objects.filter(type=WorkType.NON_VOLUNTEER).order_by('-end_date')
        return render(request, self.template_name, {'works': works})


class EducationView(TemplateView):
    template_name = 'education.html'

    def get(self, request):
        educations = Education.objects.all().order_by('-end_date')
        return render(request, self.template_name,
                      {'educations': educations})


class VolunteerView(TemplateView):
    template_name = 'volunteer.html'

    def get(self, request):
        volunteers = Work.objects.filter(type=WorkType.VOLUNTEER).order_by('-end_date')
        return render(request, self.template_name, {'volunteers': volunteers})


class AboutView(TemplateView):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name)


class ProjectsView(TemplateView):
    template_name = 'projects.html'

    def get(self, request):
        projects = Project.objects.all()
        return render(request, self.template_name, {'projects': projects})
