from django.contrib import admin

from .models import Song,Favoirite


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display =["name", "music","id"][::-1]

@admin.register(Favoirite)
class FavoiriteAdmin(admin.ModelAdmin):
    list_display = ["song"]
