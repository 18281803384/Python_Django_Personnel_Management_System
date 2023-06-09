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

from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from django.urls import path
from app01.views import Department, Personnel, Pretty, Admin, Login, Task, Order, Echarts, Uploads

urlpatterns = [
    # media相关的路由配置
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # 部门管理
    path('department/list', Department.department_list),
    path('department/add', Department.department_add),
    path('department/delete/<int:department_id>', Department.department_delete),
    path('department/edit/<int:department_id>', Department.department_edit),
    path('department/uploads', Department.department_uploads),

    # 员工管理
    path('personnel/list', Personnel.personnel_list),
    path('personnel/add', Personnel.personnel_add),
    path('personnel/model/form/add', Personnel.personnel_model_form_add),
    path('personnel/edit/<int:personnel_id>', Personnel.personnel_edit),
    path('personnel/delete/<int:personnel_id>', Personnel.personnel_delete),

    # 靓号管理
    path('pretty/list', Pretty.pretty_list),
    path('pretty/add', Pretty.pretty_add),
    path('pretty/edit/<int:pretty_id>', Pretty.pretty_edit),
    path('pretty/delete/<int:pretty_id>', Pretty.pretty_delete),

    # 管理员账户管理
    path('admin/list', Admin.admin_list),
    path('admin/add', Admin.admin_add),
    path('admin/edit/<int:admin_id>', Admin.admin_edit),
    path('admin/delete/<int:admin_id>', Admin.admin_delete),
    path('admin/reset/<int:admin_id>', Admin.admin_ps_reset),

    # 登录页面
    path('login/', Login.login),
    path('logout/', Login.logout),
    path('image/code/', Login.image_code),

    # 任务管理
    path('task/ajax', Task.task_list),
    path('task/ajax/add', Task.task_ajax_add),

    # 订单管理
    path('order/list', Order.order_list),
    path('order/add', Order.order_add),
    path('order/delete', Order.order_delete),
    path('order/detail', Order.order_detail),
    path('order/edit', Order.order_edit),

    # 数据统计
    path('echarts/list', Echarts.echarts_list),
    path('echarts/bar_data', Echarts.echarts_bar_data),
    path('echarts/line_data', Echarts.echarts_line_data),
    path('echarts/pie_data', Echarts.echarts_pie_data),

    # Form上传
    path('form/uploads/list', Uploads.form_uploads_list),

    # ModelForm上传
    path('modelform/uploads/list', Uploads.modelform_uploads_list),
]
