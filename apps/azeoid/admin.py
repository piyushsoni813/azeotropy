# azeoid/admin.py
from django.contrib import admin
from .models import StudentRegistration

# Basic admin registration
# admin.site.register(StudentRegistration)

# Customized admin registration
@admin.register(StudentRegistration)
class StudentRegistrationAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('azeoid', 'name', 'college_name', 'year_of_study', 'email', 'phone_number', 'is_verified', 'created_at')
    
    # Fields to filter by in the sidebar
    list_filter = ('year_of_study', 'college_name', 'is_verified', 'created_at')
    
    # Fields to search
    search_fields = ('azeoid', 'name', 'email', 'phone_number')
    
    # Fields to be read-only
    readonly_fields = ('azeoid', 'created_at')
    
    # Ordering of records
    ordering = ('-created_at',)
    
    # Customize the form field display
    fieldsets = (
        ('Basic Information', {
            'fields': ('azeoid', 'name', 'college_name', 'year_of_study')
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'email')
        }),
        ('Status', {
            'fields': ('is_verified', 'created_at')
        }),
    )
    
    # Number of items per page
    list_per_page = 25
    
    # Actions
    actions = ['mark_verified', 'mark_unverified']
    
    def mark_verified(self, request, queryset):
        queryset.update(is_verified=True)
    mark_verified.short_description = "Mark selected registrations as verified"

    def mark_unverified(self, request, queryset):
        queryset.update(is_verified=False)
    mark_unverified.short_description = "Mark selected registrations as unverified"
