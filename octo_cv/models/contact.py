from django.db import models

from octo_cv.constants import ContactType


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
        ('Address', ContactType.ADDRESS),
        ('Email', ContactType.EMAIL),
        ('Phone', ContactType.PHONE),
        ('Social', ContactType.SOCIAL),
    )

    type = models.CharField(max_length=20, choices=contact_types)
    name = models.CharField(max_length=30)
    description = models.TextField()
    url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
