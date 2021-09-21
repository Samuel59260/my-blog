from django.urls import path

from .views import my_view, my_new

urlpatterns = [
    path('', my_view, name='main-view'),
    path('new/', my_new, name='main-new'),
]
