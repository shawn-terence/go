from django.contrib import admin
from .models import FundingOpportunity, UserPreference, Recommendation

admin.site.register(FundingOpportunity)
admin.site.register( UserPreference)
admin.site.register(Recommendation)

# @admin.register(FundingOpportunity)
# class FundingOpportunityAdmin(admin.ModelAdmin):
#     list_display = ('title', 'sector', 'region', 'deadline')
#     search_fields = ('title', 'sector', 'region')
#     list_filter = ('sector', 'region', 'deadline')
#     ordering = ('-deadline',)

# @admin.register(UserPreference)
# class UserPreferenceAdmin(admin.ModelAdmin):
#     list_display = ('user', 'preferred_sector', 'preferred_region', 'notify_by_email')
#     search_fields = ('user__username', 'preferred_sector', 'preferred_region')
#     list_filter = ('preferred_sector', 'preferred_region', 'notify_by_email')
#     ordering = ('user',)

# @admin.register(Recommendation)
# class RecommendationAdmin(admin.ModelAdmin):
#     list_display = ('user', 'funding_opportunity', 'recommended_at', 'is_viewed')
#     search_fields = ('user__username', 'funding_opportunity__title')
#     list_filter = ('is_viewed', 'recommended_at')
#     ordering = ('-recommended_at',)