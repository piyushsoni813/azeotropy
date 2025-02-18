from django.contrib import admin
from .models import AzeoProfile

@admin.register(AzeoProfile)
class AzeoProfileAdmin(admin.ModelAdmin):
    list_display = ['azeo_id', 'user', 'college', 'department', 'year_of_study', 'verified']
    list_filter = ['verified', 'year_of_study', 'created_at']
    search_fields = ['azeo_id', 'user__username', 'user__email', 'college']
    readonly_fields = ['azeo_id', 'created_at']