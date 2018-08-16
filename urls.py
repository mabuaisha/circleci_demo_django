"""circleci_demo_django_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os

import django.contrib
import django.urls
import django.conf
from django.conf.urls.static import static


urlpatterns = [
    django.urls.path('admin/', django.contrib.admin.site.urls),
]

if os.environ.get('DJANGO_SETTINGS_MODULE') == 'settings.local':
    urlpatterns += static(django.conf.settings.STATIC_URL,
                          document_root=django.conf.settings.STATIC_ROOT)
