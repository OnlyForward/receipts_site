from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse

from accounts.forms import UserCreateForm


def index_and_sign_up(request):
    form = UserCreateForm()
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.clean()
    return render(request, 'index.html', {'form': form})


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class TestPage(TemplateView):
    template_name = 'test.html'


class HomePage(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)






