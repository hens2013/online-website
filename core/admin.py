from django.contrib import admin

from .models import Item, OrderItem, Order,  Coupon, Address, UserProfile


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'shipping_address',
                    'coupon'
                    ]
    list_display_links = [
        'user',
        'shipping_address',
        'coupon'
    ]
    list_filter = ['ordered',
                   'being_delivered',
                   'received']
    search_fields = [
        'user__username',
        'ref_code'
    ]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
    ]
    list_filter = ['country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Coupon)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile)
