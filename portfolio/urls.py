from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('work/<slug:work_slug>/', views.WorkDetailView.as_view(), name='work_detail'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]