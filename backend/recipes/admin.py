from django.contrib import admin

from .models import (Favourite, Follow, Ingredient, Recipe, RecipeIngredient,
                     Cart, Tag)


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'author',
        'favorite'
    )

    readonly_fields = ('favorite',)
    list_filter = (
        'name',
        'author',
        'tags'
    )

    def favorite(self, obj):
        return obj.favorites.count()


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'measurement_unit',
    )
    list_filter = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'color'
    )


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'author',
    )


admin.site.register(Follow, FollowAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Favourite)
admin.site.register(RecipeIngredient)
admin.site.register(Cart)
