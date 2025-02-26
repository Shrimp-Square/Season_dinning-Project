from django.contrib import admin
from markets.models import Market, MarketImage, Comment, HashTag
from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple


# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra  = 1

class MarketImageInline(admin.TabularInline):
    model = MarketImage 
    extra = 1 

class LikeUserInline(admin.TabularInline):
    model = Market.like_users.through # through는 mapping 테이블을 의미
    verbose_name = "좋아요 한 User"
    verbose_name_plural = f"{verbose_name} 목록"
    extra =1

    def has_change_permission(self, request, obj = None):
        return False
    
@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "content",
    ]
    inlines = [
        CommentInline,
        MarketImageInline,
        LikeUserInline,
    ]

    formfield_overrides = {
        ManyToManyField: {
            "widget": CheckboxSelectMultiple
        }
                           }

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "market",
        "content",
        "created",
    ]

@admin.register(MarketImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "photo",
    ]

@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    pass