from django.contrib import admin
from .models import *


class DrugAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'brand',
        'description',
        'defloration_date',
        'expiration_date'
    )

    class Meta:
        model = Drug

admin.site.register(Drug, DrugAdmin)


class ClothesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'images',
        'gender',
        'seasons',
        'description',
        'color',
        'location',
    )

    class Meta:
        model = Clothes

admin.site.register(Clothes, ClothesAdmin)


class TechAccessoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'for_tech',
        'location',
    )

    class Meta:
        model = TechAccessory

admin.site.register(TechAccessory, TechAccessoryAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'image',
        'genre',
        'author',
        'location',
    )

    class Meta:
        model = Book

admin.site.register(Book, BookAdmin)


# class ListAdmin(admin.ModelAdmin):
#     list_display = (
#         'name',
#         'books',
#         'tech',
#         'meds',
#         'clothes',
#     )
#
#     class Meta:
#         model = List
#
# admin.site.register(List, ListAdmin)
#
#
# class LendEventAdmin(admin.ModelAdmin):
#     list_display = (
#         'person',
#         'books',
#         'tech',
#         'meds',
#         'clothes',
#         'lend_start',
#         'lend_end'
#     )
#
#     class Meta:
#         model = LendEvent
#
# admin.site.register(LendEvent, LendEventAdmin)


class ClothesUseAdmin(admin.ModelAdmin):
    list_display = (
        'clothes',
        'date'
    )

    class Meta:
        model = ClothesUse

admin.site.register(ClothesUse, ClothesUseAdmin)


class TechUseAdmin(admin.ModelAdmin):
    list_display = (
        'tech',
        'date'
    )

    class Meta:
        model = TechUse

admin.site.register(TechUse, TechUseAdmin)
