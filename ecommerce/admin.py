from django.contrib import admin

from ecommerce.models import Image, Product


class ProductAdmin(admin.ModelAdmin):
    fields = (
        ('name', 'quantity'),
        'description',
        ('price', 'discount_percent'),
        'rating'
    )

    list_display = ('name', 'price', 'rating')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'featured_image')


admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)