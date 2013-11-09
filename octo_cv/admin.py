from django.contrib import admin

from octo_cv.models.contact import Contact
from octo_cv.models.education import Education


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    search_fields = ('name', 'type')


class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'degree', 'field')
    search_fields = ('school', 'degree', 'field', 'country')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Education, EducationAdmin)
