from django import forms
from .models import *


"""与models类似定义
class StudentForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=128)
    sex = forms.CharField(label='性别', choices=Student.SEX_ITEMS)
    profession = forms.CharField(label='职业', max_length=128)
    email = forms.EmailField(label='邮箱', max_length=128)
    qq = forms.CharField(label='QQ', max_length=128)
    phone = forms.CharField(label='手机', max_length=128)
"""


# 使用ModelForm复用model代码
class StudentForm(forms.ModelForm):
    # qq数字检验——表单会自动调用方法处理某个字段
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字')   # 验证失败返回错误信息
        return int(cleaned_data)

    class Meta:
        model = Student
        fields = ('name', 'sex', 'profession', 'email', 'qq', 'phone')
