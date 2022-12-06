from django.contrib import admin

from .models import (Cart,
                     Favourite,
                     Follow,
                     Ingredient,
                     Recipe,
                     RecipeIngredient,
                     Tag,
                     )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "author", "favorite")

    readonly_fields = ("favorite",)
    list_filter = ("name", "author", "tags")

    def favorite(self, obj):
        return obj.favorites.count()


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "measurement_unit",
    )
    list_filter = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "color")


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "author",
    )


admin.site.register(Favourite)
admin.site.register(RecipeIngredient)
admin.site.register(Cart)
