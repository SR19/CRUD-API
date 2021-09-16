from django.conf.urls import url
from ClientAdmin import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^admin$',views.adminApi),
    url(r'^admin/([0-9]+)$',views.adminApi),

    url(r'^client$',views.clientApi),
    url(r'^client/([0-9]+)$',views.clientApi),

    url(r'^client/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)