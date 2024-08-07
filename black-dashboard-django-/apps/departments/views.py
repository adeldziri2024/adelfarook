# departments/views.py


from django.views.generic import ListView
from .models import Department, Office

class DepartmentListView(ListView):
    model = Department
    template_name = 'home/department_list.html'
    
    def test_func(self):
        return self.request.user.is_superuser
    
class OfficeListView(ListView):
    model = Office
    template_name = 'home/office_list.html'
    
    def test_func(self):
        return self.request.user.is_superuser
    



