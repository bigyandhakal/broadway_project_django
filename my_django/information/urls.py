from django.urls import path

from information import views


urlpatterns = [

    path('about/', views.show_about, name='about'),
    path('contacts/',views.show_contacts, name='contacts'),
    path('policies', views.show_policies, name='policies'),
]