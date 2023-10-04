from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Task
from django.views.generic import ListView, UpdateView, DetailView


class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'

class TaskDetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
     model = Task
     template_name = 'update.html'
     context_object_name = 'task'
     fields = ('name','priority','date')

     def get_success_url(self):
         return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})

class TaskDeleteView(DetailView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

# Create your views here.

def demo(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date','')
        task = Task(name=name, priority=priority,date=date)
        task.save()
    return render(request, 'home.html', {'task1': task1})

def details(request):
    task = Task.objects.all()
    return render(request, 'details.html', {'task': task})

def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})
