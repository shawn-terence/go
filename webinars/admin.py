from django.contrib import admin
from .models import Webinar, WebinarRegistration, WebinarFeedback

admin.site.register(Webinar)
admin.site.register(WebinarRegistration)
admin.site.register(WebinarFeedback)


@admin.register(Webinar)
class WebinarAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker', 'date', 'is_recorded')
    search_fields = ('title', 'speaker', 'date')
    list_filter = ('date', 'is_recorded')
    ordering = ('-date',)

@admin.register(WebinarRegistration)
class WebinarRegistrationAdmin(admin.ModelAdmin):
    list_display = ('webinar', 'user', 'registered_at', 'attended')
    search_fields = ('webinar__title', 'user__username')
    list_filter = ('attended', 'registered_at')
    ordering = ('-registered_at',)

@admin.register(WebinarFeedback)
class WebinarFeedbackAdmin(admin.ModelAdmin):
    list_display = ('webinar', 'user', 'rating', 'created_at')
    search_fields = ('webinar__title', 'user__username', 'rating')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)