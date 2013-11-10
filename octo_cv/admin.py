from django.contrib import admin

from octo_cv.models import Contact, Education, Work


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    search_fields = ('name', 'type')


class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'degree', 'field')
    search_fields = ('school', 'degree', 'field', 'country')

class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'role', 'type')
    search_fields = ('type', 'company', 'role', 'city')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Work, WorkAdmin)
