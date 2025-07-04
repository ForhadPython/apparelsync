from django.shortcuts import render
from .models import (
    HomeBanner, AboutU, OurMission, OurService,
    OurValue, Leadership, OurGallery, ClientMessage,
    ContactU, ServiceContent,OurVision
)

# def home_banner_view(request):
#     banners = HomeBanner.objects.filter(is_active=True).order_by('id')
#     about_items = AboutU.objects.filter(is_active=True).order_by('id')
#
#     context = {
#         'banners': banners,
#         'about_items': about_items
#     }
#
#     return render(request, 'index.html', context)
def home_banner_view(request):
    context = {
        'banners': HomeBanner.objects.filter(is_active=True).order_by('id'),
        'about_items': AboutU.objects.filter(is_active=True).order_by('id'),
        'missions': OurMission.objects.filter(is_active=True).order_by('id'),
        'vision': OurVision.objects.filter(is_active=True).order_by('id'),
        'services': OurService.objects.filter(is_active=True).order_by('id'),
        'values': OurValue.objects.filter(is_active=True).order_by('id'),
        'leadership': Leadership.objects.filter(is_active=True).order_by('id'),
        'gallery': OurGallery.objects.filter(is_active=True).order_by('id'),
        'client_messages': ClientMessage.objects.filter(is_active=True).order_by('id'),
        'contacts': ContactU.objects.filter(is_active=True).order_by('id'),
        'service_contents': ServiceContent.objects.filter(is_active=True).order_by('id'),
    }

    return render(request, 'index.html', context)


# def about_view(request):
#     about_items = AboutU.objects.filter(is_active=True)
#     return render(request, 'about.html', {'about_items': about_items})
#
# def our_mission_view(request):
#     missions = OurMission.objects.filter(is_active=True)
#     return render(request, 'our_mission.html', {'missions': missions})
#
# def our_service_view(request):
#     services = OurService.objects.filter(is_active=True)
#     return render(request, 'our_service.html', {'services': services})
#
# def our_value_view(request):
#     values = OurValue.objects.filter(is_active=True)
#     return render(request, 'our_value.html', {'values': values})
#
# def leadership_view(request):
#     leaders = Leadership.objects.filter(is_active=True)
#     return render(request, 'leadership.html', {'leaders': leaders})
#
# def our_gallery_view(request):
#     galleries = OurGallery.objects.filter(is_active=True)
#     return render(request, 'our_gallery.html', {'galleries': galleries})
#
# def client_message_view(request):
#     messages = ClientMessage.objects.filter(is_active=True)
#     return render(request, 'client_message.html', {'messages': messages})
#
# def contact_view(request):
#     contacts = ContactU.objects.filter(is_active=True)
#     return render(request, 'contact.html', {'contacts': contacts})
#
# def service_content_view(request):
#     contents = ServiceContent.objects.filter(is_active=True)
#     return render(request, 'service_content.html', {'contents': contents})
