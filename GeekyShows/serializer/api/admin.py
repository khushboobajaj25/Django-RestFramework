from django.contrib import admin
from api import models

# Register your models here.


@admin.register(models.Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "roll", "city"]
