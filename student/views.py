from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import Student
from .forms import StudentForm
# Create your views here.


# request是Django对用户发送过来的HTTP请求的封装
def index(request):
    # 获取所有数据
    students = Student.get_all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            """手动构建Student对象并保存，如果在ModelForm中有了Model的定义，那么这些步骤可以省去
            cleaned_data = form.cleaned_data
            student = Student()
            student.name = cleaned_data['name']
            student.sex = cleaned_data['sex']
            student.email = cleaned_data['email']
            student.profession = cleaned_data['profession']
            student.qq = cleaned_data['qq']
            student.phone = cleaned_data['phone']
            student.save()
            """
            form.save()
            # reverse根据 name='index' 来拿到对应的URL
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()
    context = {'students': students, 'form': form}
    # render将上下文传入到页面进行渲染
    return render(request, 'index.html', context=context)


# 进阶view，使用class-based view——基于类的视图
# 让每一部分的功能更加明确，比如get方法就是来处理GET请求，post方法就是用来处理POST请求，维护起来更方便，不必在一个函数里改来改去
class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        students = Student.get_all()
        context = {'students': students}
        return context

    def get(self, request):
        context = self.get_context()
        form = StudentForm()
        context.update({'form': form})
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({'form': form})
        return render(request, self.template_name, context=context)
