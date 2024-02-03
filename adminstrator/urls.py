from django.urls import path 
from .views import user_login,signup, schedule_appointment, dashboard,logout_user,create_appointment,appointment_delete, update_appointment, appointment_list
app_name="adminstrator"

urlpatterns = [
    path('login',user_login,name='login'),
    path('signup',signup,name='signup'),
    path('create-appointment',schedule_appointment, name='create-appointment'),
    path('dashboard',dashboard, name='dashboard'),
    path('logout-user',logout_user,name='logout-user'),
    path('create',create_appointment,name='create-appointment'),
    path('appointment-delete/<int:id>',appointment_delete,name='appointment-delete'),
    path('appointment-update/<int:id>',update_appointment,name='appointment-update'),
    path('appointment-list',appointment_list,name='appointment-list'),


]

