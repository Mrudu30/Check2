from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add_student/',views.student_add,name='add_student'),
    path('login/',views.loginPage,name='loginpage'),
    path('show_students/',views.show_students,name='show_students'),
    path('details/<str:pk>/',views.details,name="details"),
    path('edit_details/<str:pk>/',views.edit_student,name="edit_details"),
    path('parents/<str:pk>/', views.parent_detail , name='parent_detail'),
    path('edit_parent_details/<str:pk>/',views.edit_parent,name="edit_parent_details"),
    path('students/<int:pk>/add_exam/', views.add_exam, name='add_exam'),
]
