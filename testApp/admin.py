from django.contrib import admin
from testApp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
	list_display=['eno','ename']
admin.site.register(Employee,EmployeeAdmin )
