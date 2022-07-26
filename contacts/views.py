import xlwt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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
    template_name = 'contacts/contact_form1.html'
    form_class = ContactForm

    def form_valid(self, form):
        messages.success(self.request, 'اطلاعات با موفقیت ثبت شد.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contact:form1')


class ContactCreateViewForm2(CreateView):
    model = Contact
    template_name = 'contacts/contact_form2.html'
    form_class = ContactForm

    def form_valid(self, form):
        messages.success(self.request, 'اطلاعات با موفقیت ثبت شد.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contact:form2')


def export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="contacts.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('contact')

    # Sheet header, first row
    row_num = 0
    base_style = xlwt.XFStyle()
    al = xlwt.Alignment()
    al.horz = xlwt.Alignment.HORZ_CENTER
    b_nazanin = xlwt.Font()
    b_nazanin.name = "B Nazanin"
    b_nazanin.height = 220
    num_format_str = "#,##0"

    base_style.alignment = al
    base_style.font = b_nazanin

    import copy
    header_style = copy.deepcopy(base_style)
    font_style = copy.deepcopy(base_style)
    number_style = copy.deepcopy(base_style)
    footer_style = copy.deepcopy(base_style)

    header_style.font.bold = True
    header_style.font.height = 240
    number_style.num_format_str = num_format_str
    footer_style.num_format_str = num_format_str
    footer_style.font.height = 240

    columns = (
        'ردیف',
        'نام',
        'نام خانوادگی',
        'تحصیلات',
        'شغل',
        'شماره تماس',
    )

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], header_style)

    # context = get_filtered_orders(request)
    for contact in Contact.objects.all():
        row_num += 1
        exportables = []
        exportables.append({
            'style': font_style,
            'value': row_num
        })
        exportables.append({
            'style': font_style,
            'value': contact.first_name
        })
        exportables.append({
            'style': font_style,
            'value': contact.last_name
        })
        exportables.append({
            'style': font_style,
            'value': contact.education
        })
        exportables.append({
            'style': font_style,
            'value': contact.job
        })
        exportables.append({
            'style': font_style,
            'value': contact.phone
        })

        for col_num in range(len(exportables)):
            ws.write(row_num, col_num, exportables[col_num]['value'], exportables[col_num]['style'])
    ws.cols_right_to_left = True
    wb.save(response)
    return response
