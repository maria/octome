from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from octo_cv.models import Contact, Education
from octo_cv.constants import ContactType


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get(self, request):
        """Get all the Contacts of type Social Profile or Address,
        and create a mapping:
            social_contact_name -> social_contact_object,
        in order to display them in a given order in the view.
        """
        view_social_contacts = view_contacts = dict()
        contacts = Contact.objects.filter(type__in=[ContactType.SOCIAL,
                                                    ContactType.ADDRESS])

        for contact in contacts:
            if contact.type == ContactType.SOCIAL:
                view_social_contacts[contact.name.lower()] = contact
            elif contact.type == ContactType.ADDRESS:
                view_contacts[contact.name.lower()] = contact

        template_data = {'social_contacts': view_social_contacts,
                         'contacts': view_contacts }
        return render(request, self.template_name, template_data)


class WorkView(TemplateView):
    template_name = 'work.html'

    def get(self, request):
        return render(request, self.template_name)


class EducationView(TemplateView):
    template_name = 'education.html'

    def get(self, request):
        view_educations = dict()

        educations = Education.objects.all()
        for education in educations:
            view_educations[education.degree.lower()] = education

        template_data = {'educations': view_educations}
        return render(request, self.template_name, template_data)


class VolunteerView(TemplateView):
    template_name = 'volunteer.html'

    def get(self, request):
        return render(request, self.template_name)


class AboutView(TemplateView):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name)
