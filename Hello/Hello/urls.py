# hello/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from home.views import ContactViewSet,BookingViewSet,PackageViewSet,ServiceViewSet

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'packages', PackageViewSet)
router.register(r'services', ServiceViewSet)

admin.site.site_header = "Pandey Tour and Travels Admin"
admin.site.site_title = "Pandey Tour and Travels Admin Portal"
admin.site.index_title = "Welcome to Pandey Tour and Travels"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),           # frontend
    path('api/', include(router.urls)),       # api endpoint
]
