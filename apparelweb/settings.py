"""
Django settings for apparelweb project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h^t@cv45)j$#wa0t2(4u0%13+ut2v^=dk4^1461*he_x^2^aad'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apparel',
    'django_ckeditor_5',
]


CKEDITOR_UPLOAD_PATH = "uploads/"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'apparelweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['temp'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'apparelweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-navy",
    "accent": "accent-primary",
    "navbar": "navbar-navy navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "litera",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
    "actions_sticky_top": False
}

JAZZMIN_SETTINGS = {
    "site_title": "ApparelSync",
    "site_header": "Admin",
    # "site_logo": "images/logo.png",
    "welcome_sign": "Welcome to ApparelSync",
    "copyright": "ApparelSync",
    "search_model": "account.User",
    "user_avatar": 'profile_picture',
    "icons": {
        "account": "fas fa-users-cog",
        "account.user": "fas fa-users-cog",
        "account.TempUserBeforeActive": "fas fa-star-half",

        "home.BannerSliderHome": "fas fa-sliders-h",
        "home.OurCollection": "fas fa-inbox",
        "home.FeaturedProduct": "fas fa-splotch",
        "home.LatestArrival": "fas fa-calendar-week",
        "home.ShopOurBrand": "fas fa-sliders-h",
        "home.BestSellerProduct": "fas fa-calendar-check",
        "home.BestSellerBrand": "fas fa-splotch",
        "home.GiftVoucher": "fab fa-microblog",
        "home.SocialMedia": "fas fa-icons",
        "home.MetaData": "fas fa-cloud-meatball",

        "coupons.Coupon": "fas fa-calendar-week",

        "customer.Address": "fas fa-address-card",
        "customer.Login": "fas fa-icons",
        "customer.Loyalty": "fas fa-star",
        "customer.Registration": "fas fa-puzzle-piece",

        "order.ShopCart": "fas fa-graduation-cap",
        "order.Order": "fas fa-subscript",
        "order.OrderProduct": "far fa-star",
        "order.Payment": "fas fa-money-bill-wave-alt",
        "order.Refund": "fas fa-stream",

        "product.Category": "fab fa-slideshare",
        "product.Product": "fas fa-address-card",
        "product.Images": "fas fa-bell",
        "product.Comment": "fas fa-inbox",
        "product.CommentForm": "fas fa-money-bill-wave-alt",
        "product.Color": "fas fa-file-invoice",
        "product.Size": "fab fa-monero",
        "product.Variants": "fab fa-monero",

        "data.BayEmporiumPage": "fas fa-money-bill-wave-alt",
        "data.BayEmporiumData": "fas fa-money-bill-wave-alt",
        "data.CustomerCarePage": "fas fa-money-bill-wave-alt",
        "data.CustomerCareData": "fas fa-money-bill-wave-alt",
        "data.CustomerInfoPage": "fas fa-money-bill-wave-alt",
        "data.CustomerInfoPageData": "fas fa-money-bill-wave-alt",
        "data.FollowUsPage": "fas fa-money-bill-wave-alt",
        "data.FollowUsPageData": "fas fa-money-bill-wave-alt",

    },
    "show_ui_builder": True
}
# ckeditor upload path
CKEDITOR_5_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': {
            'items': [
                'heading', '|',
                'bold', 'italic', 'underline', 'strikethrough', 'highlight', '|',
                'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', '|',
                'link', 'insertImage', 'imageUpload', 'mediaEmbed', '|',
                'bulletedList', 'numberedList', 'todoList', '|',
                'outdent', 'indent', '|',
                'alignment', '|',
                'blockQuote', 'code', 'codeBlock', '|',
                'subscript', 'superscript', '|',
                'insertTable', '|',
                'undo', 'redo', '|',
                'removeFormat', 'sourceEditing'
            ],
            'shouldNotGroupWhenFull': True
        },
        'image': {
            'toolbar': [
                'imageTextAlternative',
                '|',
                'imageStyle:inline',
                'imageStyle:block',
                'imageStyle:side',
                'linkImage'
            ],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]
        },
        'table': {
            'contentToolbar': [
                'tableColumn',
                'tableRow',
                'mergeTableCells',
                'tableProperties',
                'tableCellProperties'
            ]
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3'},
                {'model': 'heading4', 'view': 'h4', 'title': 'Heading 4', 'class': 'ck-heading_heading4'},
                {'model': 'heading5', 'view': 'h5', 'title': 'Heading 5', 'class': 'ck-heading_heading5'},
                {'model': 'heading6', 'view': 'h6', 'title': 'Heading 6', 'class': 'ck-heading_heading6'},
            ]
        },
        'list': {
            'properties': {
                'styles': True,
                'startIndex': True,
                'reversed': True,
            }
        },
        'htmlSupport': {
            'allow': [
                {
                    'name': '/.*/',
                    'attributes': True,
                    'classes': True,
                    'styles': True
                }
            ]
        },
        'removePlugins': [],
        'language': 'en'
    }
}