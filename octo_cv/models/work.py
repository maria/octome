from django.db import models

from octo_cv.constants import WorkType


class Work(models.Model):
    """Describe info about work experience. """
    class Meta:
        app_label = 'octo_cv'

    work_types = (
        (WorkType.VOLUNTEER, WorkType.VOLUNTEER),
        (WorkType.NON_VOLUNTEER, WorkType.NON_VOLUNTEER)
    )

    type = models.CharField(max_length=30, choices=work_types)
    company = models.CharField(max_length=80)
    role = models.CharField(max_length=80)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    description = models.TextField()
    url = models.URLField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    @property
    def location(self):
        return self.city + ', ' + self.country

