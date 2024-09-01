from django.contrib import admin
from .models import Expert, RetiredExpert


admin.site.register(Expert)
admin.site.register(RetiredExpert)



# @admin.register(Expert)
# class ExpertAdmin(admin.ModelAdmin):
#     list_display = ('user', 'specialization', 'rate', 'ratings', 'is_active')
#     search_fields = ('user__username', 'specialization', 'rate')
#     list_filter = ('specialization', 'is_active')
#     ordering = ('user',)

# @admin.register(RetiredExpert)
# class RetiredExpertAdmin(admin.ModelAdmin):
#     list_display = ('expert', 'years_of_experience', 'volunteer_services')
#     search_fields = ('expert__user__username', 'volunteer_services')
#     list_filter = ('years_of_experience',)
#     ordering = ('expert',)