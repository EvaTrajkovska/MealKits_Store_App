from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Buyer, )
admin.site.register(Staff, )
admin.site.register(NutrientsChart, )
admin.site.register(Menu, )
admin.site.register(Ingredient, )


class RecipeMenuAdmin(admin.TabularInline):
    model = RecipeMenu
    extra = 0


class RecipeIngredientAdmin(admin.TabularInline):
    model = RecipeIngredient
    extra = 0


class RecipeNotIncludedAdmin(admin.TabularInline):
    model = RecipeNotIncluded
    extra = 0


class RecipeNutrientsChartAdmin(admin.TabularInline):
    model = RecipeNutrientsChart
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientAdmin, RecipeNotIncludedAdmin, RecipeNutrientsChartAdmin, RecipeMenuAdmin]
    list_display = ("name",)


admin.site.register(Recipe, RecipeAdmin)

admin.site.register(NotIncluded, )
admin.site.register(ShippingAddress, )
admin.site.register(Cart, )
admin.site.register(CartItem, )
