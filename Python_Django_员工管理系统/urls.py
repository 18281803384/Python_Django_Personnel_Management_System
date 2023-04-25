"""
URL configuration for Python_Django_员工管理系统 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app01 import views

urlpatterns = [
    # 部门管理
    path('department/list', views.department_list),
    path('department/add', views.department_add),
    path('department/delete/<int:department_id>', views.department_delete),
    path('department/edit/<int:department_id>', views.department_edit),

    # 员工管理
    path('personnel/list', views.personnel_list),
    path('personnel/add', views.personnel_add),
    path('personnel/model/form/add', views.personnel_model_form_add),
    path('personnel/edit/<int:personnel_id>', views.personnel_edit),
    path('personnel/delete/<int:personnel_id>', views.personnel_delete),

    # 靓号管理
    path('pretty/list', views.pretty_list),
    path('pretty/add', views.pretty_add),
    path('pretty/edit/<int:pretty_id>', views.pretty_edit),
    path('pretty/delete/<int:pretty_id>', views.pretty_delete),
]
