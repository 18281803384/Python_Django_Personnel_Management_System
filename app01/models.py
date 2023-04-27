from django.db import models


# Create your models here.


# ------- 部门表 ------- #
class Department(models.Model):
    department_name = models.CharField(verbose_name="部门名称", max_length=36)
    create_time = models.CharField(verbose_name="创建时间", max_length=19)
    update_time = models.CharField(verbose_name="修改时间", max_length=19, null=True, blank=True, default='')

    def __str__(self):
        return self.department_name


# ------- 员工表 ------- #
class Personnel(models.Model):
    personnel_name = models.CharField(verbose_name="员工姓名", max_length=36)
    account = models.CharField(verbose_name="登录账号", max_length=36)
    password = models.CharField(verbose_name="登录密码", max_length=36)
    # 部门表被删除时（生成的数据列为 department_id ）：
    # 1.与部门表关联，当部门数据删除时，与之关联部门数据的员工信息也删除
    department = models.ForeignKey(verbose_name="部门ID", to="Department", to_field="id", on_delete=models.CASCADE)
    # 2.与部门表关联，当部门数据删除时，与之关联部门数据的员工信息的部门ID置空
    # department = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)
    # 在Django中做约束
    gender_choices = {
        (1, "男"),
        (2, "女")
    }
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    age = models.IntegerField(verbose_name="年龄")
    salary = models.DecimalField(verbose_name="薪资", max_digits=6, decimal_places=2, default=0)
    create_time = models.CharField(verbose_name="创建时间", max_length=19)
    update_time = models.CharField(verbose_name="修改时间", max_length=19, null=True, blank=True, default='')


# ------- 靓号表 ------- #
class Pretty(models.Model):
    mobile = models.CharField(verbose_name="手机号", max_length=11)
    price = models.IntegerField(verbose_name="价格")
    level_choices = {
        (1, "1级"),
        (2, "2级"),
        (3, "3级"),
        (4, "4级"),
    }
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    state_choices = {
        (1, "未使用"),
        (2, "已使用")
    }
    state = models.SmallIntegerField(verbose_name="状态", choices=state_choices, default=1)
    create_time = models.CharField(verbose_name="创建时间", max_length=19)
    update_time = models.CharField(verbose_name="修改时间", max_length=19, null=True, blank=True, default='')


# ------- 管理员表 ------- #
class Admin(models.Model):
    admin_name = models.CharField(verbose_name="管理员名称", max_length=36)
    account = models.CharField(verbose_name="登录账号", max_length=36)
    password = models.CharField(verbose_name="登录密码", max_length=36)
    create_time = models.CharField(verbose_name="创建时间", max_length=19)
    update_time = models.CharField(verbose_name="修改时间", max_length=19, null=True, blank=True, default='')






