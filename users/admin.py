from django.contrib import admin
from .models import User, Profile, Organization

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Organization)

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'role', 'is_active', 'is_staff')
#     search_fields = ('username', 'email', 'role')
#     list_filter = ('role', 'is_active', 'is_staff')
#     ordering = ('username',)

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'location', 'phone_number')
#     search_fields = ('user__username', 'location', 'phone_number')
#     ordering = ('user',)

# @admin.register(Organization)
# class OrganizationAdmin(admin.ModelAdmin):
#     list_display = ('organization_name', 'industry', 'user')
#     search_fields = ('organization_name', 'industry')
#     list_filter = ('industry',)
#     ordering = ('organization_name',)