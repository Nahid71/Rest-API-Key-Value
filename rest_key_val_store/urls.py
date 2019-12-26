
from django.contrib import admin
from django.urls import path, include
from api.views import values

urlpatterns = [
    path('admin/', admin.site.urls),
    path('values', values, name='home'),
]
