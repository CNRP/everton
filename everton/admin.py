from django.contrib import admin
from .models import NewsPost
from .models import PlayerTransfers
from .models import Fixture
from .models import Tag

class TinyMCEAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/tiny_mce/tiny_mce.js', '/static/tiny_mce/textareas.js',)

admin.site.register(NewsPost, TinyMCEAdmin)
admin.site.register(PlayerTransfers)
admin.site.register(Fixture)
admin.site.register(Tag)

admin.site.site_header = 'Everton Daily - Admin' 