from django.contrib import admin
from home.models import (Contact,
Profile)

admin.site.site_header="My Website | Second Project"



class Contact_UsAdmin(admin.ModelAdmin):
    fields = ["contact_number","name","subject","message"]

    list_display = ["id","name","contact_number","subject","message","added_on"]
    search_fields = ["name"]
    list_filter = ["added_on","name"]
    list_editable = ["name"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","cat_name","description","added_on"]

admin.site.register(Contact,Contact_UsAdmin)

admin.site.register(Profile)
