# projects/views.py

from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project
    
class ProjectListView(ListView):
    model = Project
    template_name = 'home/project_list.html'
    
    def test_func(self):
        return self.request.user.is_superuser
    
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'home/project_detail.html'
    
    def test_func(self):
        return self.request.user.is_superuser

class ProjectCreateView(UserPassesTestMixin, CreateView):
    model = Project
    fields = ['name', 'type', 'description', 'status', 'start_date', 'end_date', 'current_office', 
                    'next_office', 'priority', 'budget', 'contract_number', 'completion_percentage',
                    'risk_level', 'estimated_duration', 'notes']
    template_name = 'home/project_form.html'
    success_url = reverse_lazy('project-list')

    def test_func(self):
        return self.request.user.is_superuser

class ProjectUpdateView(UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['name', 'type', 'status', 'description', 'start_date', 'end_date', 'current_office', 
                    'next_office', 'priority', 'budget', 'contract_number', 'completion_percentage',
                    'risk_level', 'estimated_duration', 'notes']
    template_name = 'home/project_form_update.html'
    success_url = reverse_lazy('project-list')

    def test_func(self):
        return self.request.user.is_superuser

class ProjectDeleteView(UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'home/project_confirm_delete.html'
    success_url = reverse_lazy('project-list')

    def test_func(self):
        return self.request.user.is_superuser


