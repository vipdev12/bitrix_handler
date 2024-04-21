from django.contrib import admin

from .models import NamesMan, NamesWoman

# Register your models here.
admin.site.register(NamesMan)
admin.site.register(NamesWoman)