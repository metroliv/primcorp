from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'timestamp', 'parent_message', 'is_read')
    list_filter = ('timestamp', 'is_read', 'user')
    search_fields = ('message', 'user__username')  # Search by message content or username
    readonly_fields = ('timestamp',)

    # Custom form layout
    fieldsets = (
        (None, {
            'fields': ('user', 'message', 'parent_message', 'is_read')
        }),
        ('Timestamps', {
            'fields': ('timestamp',),
            'classes': ('collapse',),
        }),
    )

    # Allow replies directly in the admin interface by displaying related messages
    def parent_message_link(self, obj):
        if obj.parent_message:
            return f'<a href="/admin/chat/message/{obj.parent_message.id}/change/">{obj.parent_message.message[:30]}</a>'
        return "No parent"
    parent_message_link.allow_tags = True
    parent_message_link.short_description = 'Parent Message'

admin.site.register(Message, MessageAdmin)
