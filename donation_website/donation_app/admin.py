from django.contrib import admin
from donation_app.models import Contactform

class DonationAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Subject','Message')
# Register your models here.
admin.site.register(Contactform,DonationAdmin)