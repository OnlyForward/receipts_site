from django.shortcuts import render, render_to_response
from django.urls import reverse_lazy
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt
from django.views.generic import View, DetailView, ListView, UpdateView, DeleteView, CreateView, TemplateView
from django.http import HttpResponse

from receipts.forms import ReceiptsForm
from .models import *

# Create your views here.

package_name = 'receipts'

from django.shortcuts import render


def upload_receipts_image(instance, filename):
    return "status/{user}/{filename}".format(user=instance.user, filename=filename)


@csrf_exempt
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        # age = request.POST.get("age")     # получение значения поля age
        return HttpResponse("<h2>Hello, {0}</h2>".format(name))
    else:
        data = {'some_inf': 'jfdkasljdlkasjkl'}
        return render(request, f'{package_name}/index.html', context=data)


def sign_up_page(request):
    return render(request, f'{package_name}/sign_up_page.html')


def blogs_page(request):
    return render(request, f'{package_name}/blogs_page.html')


def sign_in_page(request):
    return render(request, f'{package_name}/sign_in_page.html')


class ReceiptsListView(ListView):
    model = Receipts
    template_name = 'receipts/receipts_list.html'
    context_object_name = 'receipts_list'


class ReceiptsDetailView(DetailView):
    model = Receipts
    template_name = 'receipts/receipts_detail.html'
    context_object_name = 'receipt_detail'


class ReceiptsDelete(DeleteView):
    model = Receipts
    success_url = reverse_lazy("receipts:list")
    context_object_name = 'receipt_delete'


class ReceiptsUpdate(UpdateView):
    model = Receipts
    fields = ("title","content")
    context_object_name = 'receipt_update'


class ReceiptsCreate(CreateView):
    # fields = ('title', 'content', 'ingredients', 'image_main')
    form_class = ReceiptsForm
    template_name = 'receipts/receipts_create.html'
    context_object_name = 'receipts_create'


