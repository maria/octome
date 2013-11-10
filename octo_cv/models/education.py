from django.db import models

from octo_cv.constants import DegreeType


class Education(models.Model):
    """Describe info about education."""
    class Meta:
        app_label = 'octo_cv'

    degree_type = (
        ('Highschool', DegreeType.HIGHSCHOOL),
        ('Bachelor', DegreeType.BACHELOR),
        ('Master', DegreeType.MASTER))

    school = models.CharField(max_length=60)
    degree = models.CharField(max_length=60, choices=degree_type)
    field = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    @property
    def location(self):
        return self.city + ', ' + self.country

