from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class HomeBanner(models.Model):
    image = models.ImageField(upload_to='HomeBanner', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    description = CKEditor5Field(config_name='default', blank=True, null=True)
    banner_content = CKEditor5Field(config_name='default', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or ""


class AboutU(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = CKEditor5Field(config_name='default', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or ""


class OurMission(models.Model):
    image = models.ImageField(upload_to='OurMission', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = CKEditor5Field(config_name='default', blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or ""


class OurVision(models.Model):
    image = models.ImageField(upload_to='OurMission', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = CKEditor5Field(config_name='default', blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or ""


class OurService(models.Model):
    image = models.ImageField(upload_to='OurServices', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = CKEditor5Field(config_name='default', blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or ""


class OurValue(models.Model):
    image = models.ImageField(upload_to='OurValues', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = CKEditor5Field(config_name='default')
    link = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or ""


class Leadership(models.Model):
    image = models.ImageField(upload_to='Leadership', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = CKEditor5Field(config_name='default', blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or ""


class OurGallery(models.Model):
    image = models.ImageField(upload_to='OurGallery', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or ""


class ContactU(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    message = CKEditor5Field(config_name='default', blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or ""


class SiteInfo(models.Model):
    company_name = models.CharField(max_length=200, blank=True, null=True)
    address_line1 = models.CharField(max_length=200, blank=True, null=True)
    city_state_zip = models.CharField(max_length=200, blank=True, null=True)  # could be city, state, zip or full address
    facebook_link = models.URLField(max_length=400, blank=True, null=True)  # optional for social link
    instagram_link = models.URLField(max_length=400, blank=True, null=True)  # optional for social link
    phone = models.CharField(max_length=50, blank=True, null=True)  # optional for phone number
    favicon = models.ImageField(upload_to='favicons/', blank=True, null=True)  # optional for favicon image

    def __str__(self):
        return self.company_name or "Unnamed SiteInfo"


class NavItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)  # could be internal anchor (#home) or full URL
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


# Optional social links or footer links can be added similarly

class ProductKnit(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name


class ProductWoven(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name


class ProductSweater(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name


class ProductHomeTextile(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
