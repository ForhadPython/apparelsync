from django.shortcuts import render
from .models import (
    HomeBanner, AboutU, OurMission, OurVision,
    OurService, OurValue, Leadership, OurGallery,
    ContactU, SiteInfo, ProductKnit, ProductWoven, ProductSweater, ProductHomeTextile
)

def home_page(request):
    banners = HomeBanner.objects.filter(is_active=True)
    about = AboutU.objects.filter(is_active=True).first()
    mission = OurMission.objects.filter(is_active=True)
    vision = OurVision.objects.filter(is_active=True)
    services = OurService.objects.filter(is_active=True)
    values = OurValue.objects.filter(is_active=True)
    leadership = Leadership.objects.filter(is_active=True)
    gallery = OurGallery.objects.filter(is_active=True)
    contact = ContactU.objects.filter(is_active=True).first()
    site_info = SiteInfo.objects.first()

    context = {
        'banners': banners,
        'about': about,
        'mission': mission,
        'vision': vision,
        'services': services,
        'values': values,
        'leadership': leadership,
        'gallery': gallery,
        'contact': contact,
        'site_info': site_info,
    }
    return render(request, 'index.html', context)

# def about_view(request):
#     about = AboutU.objects.filter(is_active=True)
#     return render(request, 'about.html', {'about': about})
#
# def mission_view(request):
#     mission = OurMission.objects.filter(is_active=True)
#     return render(request, 'mission.html', {'mission': mission})
#
# def vision_view(request):
#     vision = OurVision.objects.filter(is_active=True)
#     return render(request, 'vision.html', {'vision': vision})
#
# def service_view(request):
#     services = OurService.objects.filter(is_active=True)
#     return render(request, 'services.html', {'services': services})
#
# def value_view(request):
#     values = OurValue.objects.filter(is_active=True)
#     return render(request, 'values.html', {'values': values})
#
# def leadership_view(request):
#     leaders = Leadership.objects.filter(is_active=True)
#     return render(request, 'leadership.html', {'leaders': leaders})
#
# def gallery_view(request):
#     gallery = OurGallery.objects.filter(is_active=True)
#     return render(request, 'gallery.html', {'gallery': gallery})
#
# def contact_view(request):
#     contact = ContactU.objects.filter(is_active=True)
#     return render(request, 'contact.html', {'contact': contact})

def knit_products(request):
    products = ProductKnit.objects.all()
    return render(request, 'knit.html', {'products': products})

def woven_products(request):
    products = ProductWoven.objects.all()
    return render(request, 'woven.html', {'products': products})

def sweater_products(request):
    products = ProductSweater.objects.all()
    return render(request, 'sweater.html', {'products': products})

def home_textile_products(request):
    products = ProductHomeTextile.objects.all()
    return render(request, 'home_textile.html', {'products': products})