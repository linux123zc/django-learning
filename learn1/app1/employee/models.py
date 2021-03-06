from django.db import models

# Create your models here.

# 员工数据模型 （员工数据表）
class employee(models.Model):
    # 员工姓名
    name = models.CharField(max_length=32, verbose_name="姓名")
    # 员工邮箱
    email = models.EmailField(verbose_name="邮箱")
    # 员工部门， Foreignkey 类型， 与department 表中记录形成多对一的关系
    dep = models.ForeignKey(to='department', on_delete=models.CASCADE)
    # 员工加入的团体，多对多关系
    group = models.ManyToManyField(to='group')
    # 薪水
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    # 员工补充信息
    info = models.OneToOneField(to='employeeinfo', on_delete=models.CASCADE, null=True)

# 部门数据模型 （部门数据表）
class department(models.Model):
    # 部门名称
    dep_name = models.CharField(max_length=32, verbose_name='部门名称')
    # 部门备注
    dep_script = models.CharField(max_length=60, verbose_name='备注')

# 团体数据模型 (团体数据表)
class group(models.Model):
    # 团体名称
    group_name = models.CharField(max_length=32, verbose_name='团体名称')
    # 团体备注
    group_script = models.CharField(max_length=60, verbose_name='备注')

# 员工补充信息模型 （员工补充信息表）
class employeeinfo(models.Model):
    # 电话号码
    phone = models.CharField(max_length=11)
    # 地址
    address = models.CharField(max_length=50)