from django.contrib import admin
from .models import Partnership, PartnershipRequest

admin.site.register(Partnership)
admin.site.register(PartnershipRequest)

@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    list_display = ('organization', 'partner_organization', 'status', 'created_at')
    search_fields = ('organization__organization_name', 'partner_organization__organization_name')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)

@admin.register(PartnershipRequest)
class PartnershipRequestAdmin(admin.ModelAdmin):
    list_display = ('organization', 'partner_organization', 'is_approved', 'created_at')
    search_fields = ('organization__organization_name', 'partner_organization__organization_name')
    list_filter = ('is_approved', 'created_at')
    ordering = ('-created_at',)