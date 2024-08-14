from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Buyer)
admin.site.register(Game)
admin.site.register(Post)
# admin.site.register(CustomUser)
# admin.site.register(Cart)
# admin.site.register(CartItem)
#
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'category',)
#     filds = [('name', 'price'), 'discription', 'image', 'category'] #объединяем вывод
#     search_fields = ('name',)
#     list_filter = ('price', 'category', )
    # fieldsets = (('test1', {'fieds'}:('name', 'price', 'category')}),
