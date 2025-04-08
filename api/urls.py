from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView),
    path('student/<int:pk>/', views.studentDetailView),
    
    
    path('employees/', views.Employees.as_view()), #this as_view() means it is a class based view
    path('employee/<int:pk>/',views.EmployeeDetail.as_view()),
    
    
] 
