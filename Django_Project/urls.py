"""Django_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',views.index,name="main"),
    path('validate',views.validate,name="validate"),
    path('shedule_new',views.shedule_new,name="shedule_new"),
    path('register',views.register_class,name="register"),
    path('view_all_class',views.view_all_class,name="view_all_class"),

    path('update_class/',views.update_class,name="update"),
    path('save_update/',views.save_update,name="save_update"),

   # path('allcourse/',views.allcourse,name="allcourse"),
    path('delete_class/', views.delete_class, name="delete_class"),
    path('student_index/',views.student_index,name="student_index"),
    path('student_registration/',views.student_registration,name="student_registration"),
    path('save_registration/',views.save_registration,name="save_registration"),
    path('student_login/',views.student_login,name="student_login"),
    path('login_validation/',views.login_validation,name="login_validation"),

    path('OpenFacbook/',views.OpenFacbook.as_view(),name="OpenFacbook"),
    path('welcome_page/',TemplateView.as_view(template_name="welcome_page.html"),name="welcome_page"),
    path('enrol_course/',views.enrol_course.as_view(),name="enroll"),
    path('view_all_enroll/',views.view_all_enroll.as_view(),name="view_all_enroll"),
    path('cancel_class<int:pk>/',views.cancel_class.as_view(),name="cancel_class")



]
