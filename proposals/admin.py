from django.contrib import admin
from .models import Template, ProjectProposal

admin.site.register(Template)
admin.site.register(ProjectProposal)

# @admin.register(ProjectProposal)
# class ProjectProposalAdmin(admin.ModelAdmin):
#     list_display = ('client', 'title', 'sector', 'status', 'created_at')
#     search_fields = ('client__username', 'title', 'sector')
#     list_filter = ('sector', 'status', 'created_at')
#     ordering = ('created_at',)

# @admin.register(Template)
# class TemplateAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'price', 'is_free')
#     search_fields = ('title', 'category')
#     list_filter = ('category', 'is_free')
#     ordering = ('title',)