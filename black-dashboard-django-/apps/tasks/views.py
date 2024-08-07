# tasks/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'home/task_list.html'
    
    def test_func(self):
        return self.request.user.is_superuser

class TaskDetailView(DetailView):
    model = Task
    template_name = 'home/Task_detail.html'
    
    def test_func(self):
        return self.request.user.is_superuser
    
class TaskCreateView(CreateView):
    model = Task
    fields = ['name', 'description', 'project', 'assigned_to', 'office', 'status', 'due_date']
    template_name = 'home/task_form.html'
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['name', 'description', 'project', 'assigned_to', 'office', 'status', 'due_date']
    template_name = 'home/task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'home/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

