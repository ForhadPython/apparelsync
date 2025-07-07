from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('knit/', views.knit_products, name='knit_products'),
    path('woven/', views.woven_products, name='woven_products'),
    path('sweater/', views.sweater_products, name='sweater_products'),
    path('home-textile/', views.home_textile_products, name='home_textile_products'),
    # path('mission/', views.mission_view, name='mission'),
    # path('vision/', views.vision_view, name='vision'),
    # path('services/', views.service_view, name='services'),
    # path('values/', views.value_view, name='values'),
    # path('leadership/', views.leadership_view, name='leadership'),
    # path('gallery/', views.gallery_view, name='gallery'),
    # path('contact/', views.contact_view, name='contact'),
]
