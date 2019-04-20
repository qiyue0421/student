from django.contrib import admin
from .models import Student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ('id', 'name', 'sex', 'profession', 'email', 'qq', 'phone', 'status', 'created_time')
    # 过滤器
    list_filter = ('sex', 'status', 'created_time')
    # 可搜索字段
    search_fields = ('name', 'profession')
    fieldsets = (       # fieldsets 是一个以二元元组为元素的列表, 每一个二元元组代表一个在管理表单
        (
            None, {   # 二元元组的格式是 (name, field_options), 其中 name 是一个字符串相当于 fieldset的标题，为None表示无标题
                'fields': ('name', ('sex', 'profession'), ('email', 'qq', 'phone'), 'status',)
            }    # sex、profession显示同一行，email、qq、phone显示在同一行
        ),
    )


# 注册
admin.site.register(Student, StudentAdmin)
