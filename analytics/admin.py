from django.contrib import admin

from .models import ObjectViewed
# Register your models here.

class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'content_object', 'timestamp')
    change_list_template = 'admin/objectviewedadmin.html'

admin.site.register(ObjectViewed, AnalyticsAdmin)