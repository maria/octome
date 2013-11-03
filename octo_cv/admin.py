from django.contrib import admin

from octo_cv.models.contact import Contact


class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contact, ContactAdmin)
