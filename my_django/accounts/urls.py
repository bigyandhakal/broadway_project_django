from django.urls import path

from accounts import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('register',views.register, name='register'),
    path('register_user',views.register_user, name='register_user'),
    path('user_login',views.user_login, name='user_login'),
    path('logout',views.logout, name='logout'),
    path('profile',views.profile, name='profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('org_register',views.org_register, name='org_register'),
    path('register_org',views.register_org, name='register_org'),

]