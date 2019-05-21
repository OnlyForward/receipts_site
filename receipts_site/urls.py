"""receipts_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from receipts.views import index
from receipts_site.views import HomePage, TestPage, ThanksPage

urlpatterns = [
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r"^test/$", TestPage.as_view(), name="test"),
    url(r'^receipts/', include('receipts.urls',namespace='receipts')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^thanks/$', ThanksPage.as_view(), name='thanks'),
    url(r'^receipts/api/',include('receipts.api.urls')),
    url(r"^posts/", include("posts.urls", namespace="posts")),
    url(r"^groups/", include("groups.urls", namespace="groups")),
    # url(r"^groups/", include("groups.urls", namespace="groups")),
    # url(r"^posts/", include("posts.urls", namespace="posts"))
]
