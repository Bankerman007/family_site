from django.contrib import admin
from . models import Events,Issue,Need,Repair

admin.site.register(Events)
admin.site.register(Issue)
admin.site.register(Need)
admin.site.register(Repair)
