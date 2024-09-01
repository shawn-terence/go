from django.contrib import admin
from .models import Rating, AverageRating

admin.site.register(Rating)
admin.site.register(AverageRating)

# @admin.register(Rating)
# class RatingAdmin(admin.ModelAdmin):
#     list_display = ('user', 'content_type', 'object_id', 'rating', 'created_at')
#     search_fields = ('user__username', 'content_type__model', 'rating')
#     list_filter = ('rating', 'created_at')
#     ordering = ('-created_at',)

# @admin.register(AverageRating)
# class AverageRatingAdmin(admin.ModelAdmin):
#     list_display = ('content_type', 'object_id', 'average_rating', 'rating_count')
#     search_fields = ('content_type__model',)
#     ordering = ('-average_rating',)