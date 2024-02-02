from django.urls import path 
from .views import user_login,signup, schedule_appointment, dashboard,logout_user
app_name="adminstrator"

urlpatterns = [
    path('login',user_login,name='login'),
    path('signup',signup,name='signup'),
    path('create-appointment',schedule_appointment, name='create-appointment'),
    path('dashboard',dashboard, name='dashboard'),
    path('logout-user',logout_user,name='logout-user')


]

