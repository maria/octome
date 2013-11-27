from django.db import models

from octo_cv.constants import ContactType, NetworkType

class Contact(models.Model):
    """Describe a contact information resource, like a social profile.
    Example:
        Twitter Contact:
            - name - Twitter
            - link - link to Twitter profile
            - image - Twitter logo
            - description - account description
    """
    class Meta:
        app_label = 'octo_cv'

    contact_types = (
        (ContactType.ADDRESS, ContactType.ADDRESS),
        (ContactType.EMAIL, ContactType.EMAIL),
        (ContactType.PHONE, ContactType.PHONE),
        (ContactType.SOCIAL, ContactType.SOCIAL),
        (ContactType.SKYPE, ContactType.SKYPE)
    )

    network_types = (
        (NetworkType.PROFESSIONAL, NetworkType.PROFESSIONAL),
        (NetworkType.SOCIAL, NetworkType.SOCIAL),
        (NetworkType.GENERAL, NetworkType.GENERAL)
    )

    type = models.CharField(max_length=20, choices=contact_types)
    name = models.CharField(max_length=30)
    description = models.TextField()
    url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    network = models.CharField(max_length=30, choices=network_types, null=True,
                              help_text="Return the type of network for the "
                              "social profile, in order to display the Linkedin,"
                              " GH accounts before Pinterest or Twitter  accounts.")
