from django.contrib import admin
from django.utils.html import format_html
from .models import (
    HomeBanner,
    AboutU,
    OurMission,
    OurService,
    OurValue,
    Leadership,
    OurGallery,
    ClientMessage,
    ContactU,
    SiteInfo,
    NavItem,
)

@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'link')
    list_filter = ('is_active',)
    search_fields = ('title', 'link')
    ordering = ('-is_active', 'title')

@admin.register(AboutU)
class AboutUAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'link')
    list_filter = ('is_active',)
    search_fields = ('title', 'link')
    ordering = ('-is_active', 'title')

@admin.register(OurMission)
class OurMissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'link')
    list_filter = ('is_active',)
    search_fields = ('title', 'link')
    ordering = ('-is_active', 'title')
    readonly_fields = ('image_preview1', 'image_preview2', 'image_preview3')

    def image_preview1(self, obj):
        if obj.image1:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image1.url)
        return "-"
    image_preview1.short_description = 'Image 1 Preview'

    def image_preview2(self, obj):
        if obj.image2:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image2.url)
        return "-"
    image_preview2.short_description = 'Image 2 Preview'

    def image_preview3(self, obj):
        if obj.image3:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image3.url)
        return "-"
    image_preview3.short_description = 'Image 3 Preview'


@admin.register(OurService)
class OurServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'link')
    list_filter = ('is_active',)
    search_fields = ('title', 'link')
    ordering = ('-is_active', 'title')
    readonly_fields = ('image_preview1', 'image_preview2', 'image_preview3')

    def image_preview1(self, obj):
        if obj.image1:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image1.url)
        return "-"
    image_preview1.short_description = 'Image 1 Preview'

    def image_preview2(self, obj):
        if obj.image2:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image2.url)
        return "-"
    image_preview2.short_description = 'Image 2 Preview'

    def image_preview3(self, obj):
        if obj.image3:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image3.url)
        return "-"
    image_preview3.short_description = 'Image 3 Preview'

@admin.register(OurValue)
class OurValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'link')
    list_filter = ('is_active',)
    search_fields = ('title', 'link')
    ordering = ('-is_active', 'title')
    readonly_fields = ('image_preview1', 'image_preview2', 'image_preview3')

    def image_preview1(self, obj):
        if obj.image1:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image1.url)
        return "-"
    image_preview1.short_description = 'Image 1 Preview'

    def image_preview2(self, obj):
        if obj.image2:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image2.url)
        return "-"
    image_preview2.short_description = 'Image 2 Preview'

    def image_preview3(self, obj):
        if obj.image3:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image3.url)
        return "-"
    image_preview3.short_description = 'Image 3 Preview'

@admin.register(Leadership)
class LeadershipAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'link')
    list_filter = ('is_active',)
    search_fields = ('title', 'link')
    ordering = ('-is_active', 'title')
    readonly_fields = ('image_preview1', 'image_preview2', 'image_preview3')

    def image_preview1(self, obj):
        if obj.image1:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image1.url)
        return "-"
    image_preview1.short_description = 'Image 1 Preview'

    def image_preview2(self, obj):
        if obj.image2:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image2.url)
        return "-"
    image_preview2.short_description = 'Image 2 Preview'

    def image_preview3(self, obj):
        if obj.image3:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image3.url)
        return "-"
    image_preview3.short_description = 'Image 3 Preview'

@admin.register(OurGallery)
class OurGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'link', 'image_preview')
    list_filter = ('is_active',)
    search_fields = ('title', 'link')
    ordering = ('-is_active', 'title')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'

@admin.register(ClientMessage)
class ClientMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'message')
    ordering = ('-is_active', 'title')

@admin.register(ContactU)
class ContactUAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
    ordering = ('-is_active', 'title')


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'address_line1', 'city_state_zip', 'phone', 'author')
    # Since you usually want only one SiteInfo, you can prevent adding multiple:
    def has_add_permission(self, request):
        # Allow adding only if no SiteInfo exists yet
        if SiteInfo.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(NavItem)
class NavItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order')
    list_editable = ('order',)
    ordering = ('order',)
