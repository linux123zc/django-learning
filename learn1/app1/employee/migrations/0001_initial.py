# Generated by Django 2.2 on 2021-03-06 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=32, verbose_name='部门名称')),
                ('dep_script', models.CharField(max_length=60, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='employeeinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=32, verbose_name='团体名称')),
                ('group_script', models.CharField(max_length=60, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.department')),
                ('group', models.ManyToManyField(to='employee.group')),
                ('info', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employeeinfo')),
            ],
        ),
    ]
