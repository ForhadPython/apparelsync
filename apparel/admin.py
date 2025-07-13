from django.contrib import admin
from .models import (
    HomeBanner, AboutU, OurMission, OurVision,
    OurService, OurValue, Leadership, OurGallery,
    ContactU, SiteInfo, NavItem, ProductKnit, ProductWoven, ProductSweater, ProductHomeTextile
)


@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'link')
    fieldsets = (
        ('Banner Details', {
            'fields': ('image', 'title', 'link', 'is_active')
        }),
        ('Content', {
            'fields': ('description', 'banner_content')
        }),
    )


@admin.register(AboutU)
class AboutUAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
    fields = ('title', 'description', 'is_active')


@admin.register(OurMission)
@admin.register(OurVision)
@admin.register(OurService)
@admin.register(Leadership)
class CommonAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'link')
    fields = ('image', 'title', 'description', 'link', 'is_active')


@admin.register(OurValue)
class OurValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'link')
    fields = ('image', 'title', 'description', 'link', 'is_active')


@admin.register(OurGallery)
class OurGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'link')
    fields = ('image', 'title', 'link', 'is_active')


@admin.register(ContactU)
class ContactUAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'link')
    fields = ('title', 'message', 'link', 'is_active')


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'phone', 'facebook_link', 'instagram_link')
    search_fields = ('company_name', 'address_line1', 'city_state_zip')
    list_filter = ('company_name',)
    fieldsets = (
        (None, {
            'fields': ('company_name', 'address_line1', 'city_state_zip', 'phone')
        }),
        ('Social Media', {
            'fields': ('facebook_link', 'instagram_link')
        }),
        ('Other', {
            'fields': ('favicon',)
        }),
    )


# @admin.register(NavItem)
# class NavItemAdmin(admin.ModelAdmin):
#     list_display = ('name', 'url', 'order')
#     search_fields = ('name', 'url')
#     ordering = ('order',)


@admin.register(ProductKnit)
class ProductKnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)


@admin.register(ProductWoven)
class ProductWovenAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)


@admin.register(ProductSweater)
class ProductSweaterAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)


@admin.register(ProductHomeTextile)
class ProductHomeTextileAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)
