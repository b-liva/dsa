from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContactListView.as_view(), name='index'),
    path('add', views.ContactCreateView.as_view(), name='add'),
]