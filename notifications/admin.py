from django.contrib import admin
from .models import Notification, RoleBasedNotification


admin.site.register(Notification)
admin.site.register(RoleBasedNotification)



@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'notification_type', 'message', 'is_read', 'created_at')
    search_fields = ('user__username', 'notification_type', 'message')
    list_filter = ('notification_type', 'is_read', 'created_at')
    ordering = ('-created_at',)

@admin.register(RoleBasedNotification)
class RoleBasedNotificationAdmin(admin.ModelAdmin):
    list_display = ('role', 'notification')
    search_fields = ('role', 'notification__message')
    ordering = ('role',