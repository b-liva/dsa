from django.urls import path

from . import views

app_name = 'contact'
urlpatterns = [
    path('', views.ContactListView.as_view(), name='index'),
    path('form1', views.ContactCreateView.as_view(), name='form1'),
    path('form2', views.ContactCreateViewForm2.as_view(), name='form2'),
    path('export', views.export, name='export'),
]
