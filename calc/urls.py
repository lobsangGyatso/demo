from django.urls import path


from . import  views

urlpatterns=[
    path('',views.home,name='home'),
    path('addtwonumber',views.addtwonumber,name='addtwonumber'),
    path('registration',views.registration,name="registration"),
    path('login',views.login,name="login"),
    path('employee_list',views.employee_list,name='employee_list'),
    path('employee_form',views.employee_form,name='employee_form'),
    path('show',views.show, name='show'), 
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')

]

