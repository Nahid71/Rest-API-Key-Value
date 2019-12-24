from django.urls import path
from .views import values

urlpatterns = {
    path('values', values, name="values"),
}
