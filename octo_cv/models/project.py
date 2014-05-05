from django.db import models


class Project(models.Model):

    class Meta:
        app_label = 'octo_cv'

    name = models.CharField(max_length=30)
    description = models.TextField()
    url = models.URLField(null=True, blank=True)
