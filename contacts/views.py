from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Contact
# Create your views here.
from django.http import HttpResponse


class ContactListView(ListView):
    model = Contact
    context_object_name = 'contacts'


class ContactCreateView(CreateView ):
    model = Contact
    fields = ('first_name', 'last_name', 'phone', 'job', 'education')

    success_url = "/contacts"
