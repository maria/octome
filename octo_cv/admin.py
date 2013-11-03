from django.contrib import admin

from octo_cv.models.contact import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    search_fields = ('name', 'type')


admin.site.register(Contact, ContactAdmin)
