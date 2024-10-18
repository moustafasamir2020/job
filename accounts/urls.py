from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup,name='sign'),
    path('log_out/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    
    
]