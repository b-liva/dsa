from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Contact
# Create your views here.
from django.http import HttpResponse


class ContactListView(ListView):
    model = Contact
    context_object_name = 'contacts'
