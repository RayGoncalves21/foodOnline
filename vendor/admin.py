from django.contrib import admin

from vendor.models import Vendor


class VendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'vendor_name', 'is_aproved',
                    'created_at', 'vendor_license')
    list_display_links = ('user', 'vendor_name')
    list_editable = ('is_aproved',)


admin.site.register(Vendor, VendorAdmin)
