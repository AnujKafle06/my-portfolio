from django.contrib import admin
from .models import Skill

# Register your models here.


# class skills(admin.ModelAdmin):
#     list_display= ('name', 'img')

admin.site.register(Skill)