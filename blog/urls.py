from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    # path('', views.home, name='blog-home'),
    # path('about/', views.about, name='blog-about'),
    path('', views.button),
    path('output/', views.output, name='script'),
    path('external/', views.external),
 ]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

