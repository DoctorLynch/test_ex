from django.contrib import admin

from birds.models import Birds, ViewBirds


@admin.register(Birds)
class BirdsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(ViewBirds)
class View_BirdsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
