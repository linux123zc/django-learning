#!/usr/bin/python
# codeing: utf-8

from django.shortcuts import render, redirect, HttpResponse
from .models import employee, department, group, employeeinfo

# Create your views here.

def list_dep_old(request):
    dep_list = department.objects.all()
    return render(request, 'test_orm_old/list_dep_old.html', {'dep_list':dep_list})

def add_dep_old(request):
    # 判断请求方式， 如果是 POST， 说明前端页面要提交数据
    if request.method == 'POST':
        dep_name = request.POST.get('dep_name')
        dep_script = request.POST.get('dep_script')
        if dep_name.strip() == '':
            return render(request, 'test_orm_old/add_dep_old.html', {'error_info':'部门名称不能为空'})
        try:
            # 用create()函数创建一条记录，这条记录会自动保存，不用调用save函数
            # obj = department(dep_name=dep_name, dep_script=dep_script)
            # obj.save()
            p = department.objects.create(dep_name=dep_name, dep_script=dep_script)
            return redirect('/test_orm_old/list_dep_old/')
        except Exception as e:
            return render(request, 'test_orm_old/add_dep_old.html', {'error_inifo':'输入部门名称重复或者信息有错误!'})
        finally:
            pass

    return render(request, 'test_orm_old/add_dep_old.html')

def del_dep_old(request, dep_id):
    # 通过 get() 函数取得一条记录
    dep_object = department.objects.get(id=dep_id)
    # 删除部门记录
    dep_object.delete()
    return redirect('/test_orm_old/list_dep_old/')

def edit_dep_old(request, dep_id):
    # 判断请求方式
    if request.method == 'POST':
        id = request.POST.get('id')
        # 获取前端页面提交的数据
        dep_name = request.POST.get('dep_name')
        dep_script = request.POST.get('dep_script')
        dep_object = department.objects.get(id=id)
        # 给字段赋值
        dep_object.dep_name = dep_name
        dep_object.dep_script = dep_script
        # 保存数据到数据库
        dep_object.save()
        return redirect('/test_orm_old/list_dep_old/')
    else:
        dep_object = department.objects.get(id=dep_id)
        return render(request, 'test_orm_old/edit_dep_old.html', {'department':dep_object})
