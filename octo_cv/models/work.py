from django.db import models


class Work(models.Model):
    """Describe info about work experience. """
    class Meta:
        app_label = 'octo_cv'

    company = models.CharField(max_length=60)
    role = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    description = models.TextField()
    url = models.URLField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    @property
    def location(self):
        return self.city + ', ' + self.country

