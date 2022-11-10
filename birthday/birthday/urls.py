from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('birthday_show.urls')),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
