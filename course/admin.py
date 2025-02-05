from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Course


class CourseAdmin(TranslatableAdmin):
    list_display = ('title', 'description')

admin.site.register(Course, CourseAdmin)