from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_banner_view, name='home_banner'),
    # path('about/', views.about_view, name='about'),
    # path('our-mission/', views.our_mission_view, name='our_mission'),
    # path('our-service/', views.our_service_view, name='our_service'),
    # path('our-value/', views.our_value_view, name='our_value'),
    # path('leadership/', views.leadership_view, name='leadership'),
    # path('our-gallery/', views.our_gallery_view, name='our_gallery'),
    # path('client-message/', views.client_message_view, name='client_message'),
    # path('contact/', views.contact_view, name='contact'),
    # path('service-content/', views.service_content_view, name='service_content'),
]
