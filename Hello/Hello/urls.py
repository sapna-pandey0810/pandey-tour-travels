from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Pandey Tour and Travels Admin"
admin.site.site_title = "Pandey Tour and Travels Admin Portal"
admin.site.index_title = "Welcome to Pandey Tour and Travels"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]