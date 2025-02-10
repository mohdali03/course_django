from django.contrib import admin

# Register your models here.
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    def fees(self, obj):
        return obj.fee
    fees.short_description = 'Fees'
    
    def description(self, obj):
        return obj.desc
    description.short_description = 'description'

    list_display = ('name', 'duration', 'description', 'fees')
    search_fields = ('name', 'fee')
    list_filter = ('duration', 'fee')
    
admin.site.register(Course, CourseAdmin)
