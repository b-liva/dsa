from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, CreateView

from .forms import ContactForm
from .models import Contact
# Create your views here.


class ContactListView(ListView):
    model = Contact
    context_object_name = 'contacts'


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm

    def form_valid(self, form):
        messages.success(self.request, 'اطلاعات با موفقیت ثبت شد.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contact:add')
