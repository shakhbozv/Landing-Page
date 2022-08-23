from django.contrib import admin

# Register your models here.
from .models import Project, Developer, Skill

admin.site.register(Project),
admin.site.register(Developer),
admin.site.register(Skill),