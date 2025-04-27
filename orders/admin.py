from django.contrib import admin
from .models import Order

# Create a custom admin class for the Order model
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_email', 'system', 'service', 'quantity', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer_name', 'customer_email')
    ordering = ('-created_at',)
    list_per_page = 10

    # Optionally, you can define form fields for a more customized layout
    fields = ('customer_name', 'customer_email', 'system', 'service', 'quantity', 'status', 'created_at')
    readonly_fields = ('created_at',)

# Register the Order model with the custom admin class
admin.site.register(Order, OrderAdmin)
