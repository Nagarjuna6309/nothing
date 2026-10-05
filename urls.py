"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from core.views import home, tv_status,tv_power,tv_volume,bluetooth_connect,wifi_connect,audio_test,audio_start

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("api/tv/status/", tv_status, name="tv_status"),
    path("api/tv/power/", tv_power, name="tv_power"),
    path("api/tv/volume/", tv_volume, name="tv_volume"),
    path("api/bluetooth/connect/", bluetooth_connect, name="bluetooth_connect"),
    path("api/wifi/connect/", wifi_connect, name="wifi_connect"),
    path("api/audio/test/", audio_test, name="audio_test"),
    path("api/audio/start/", audio_start, name="audio_start"),
]
