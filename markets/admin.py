from django.contrib import admin
from markets.models import Market, Festival_id, HashTag, MarketImage
# Register your models here.

@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    pass

@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    pass

@admin.register(Festival_id)
class Festival_idAdmin(admin.ModelAdmin):
    pass

@admin.register(MarketImage)
class MarketImageAdmin(admin.ModelAdmin):
    pass