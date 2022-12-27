from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from ApiEmp.models.models import District, Thana, Department, Designation, \
                                EmpBasicInfo, EmpSalary, EmpEducation

# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
    list_display=['id', 'name']
    list_filter=['id', 'name']
    search_fields = ['name']
    ordering = ['id'] 

class ThanaAdmin(admin.ModelAdmin):
    list_display=['id','district','name']
    list_filter=['id','district','name']
    ordering = ['id']

class DepartmentAdmin(admin.ModelAdmin):
    list_display=['id','name']
    list_filter=['id','name']
    ordering = ['id'] 

class DesignationAdmin(admin.ModelAdmin):
    list_display=['id','name']
    list_filter=['id','name']
    ordering = ['id']

class EmpBasicInfoAdmin(admin.ModelAdmin):
    list_display=[
                    'id', 'emp_id','first_name', 'last_name', 
                    'dob_tag', 'image_tag', 'phone', 'email', 
                    'thana', 'district', 'joiningdate_tag', 
                    'department', 'designation', 'status'
            ]

class EmpSalaryAdmin(admin.ModelAdmin):
    list_display=['employee', 'basicsalary', 'medical', 'houserent', 'others', ]

class EmpEducationAdmin(admin.ModelAdmin):
    list_display=['employee', 'degree', 'institute', 'passingyear', 'result']

admin.site.register(District, DistrictAdmin)
admin.site.register(Thana, ThanaAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(EmpBasicInfo, EmpBasicInfoAdmin)
admin.site.register(EmpSalary, EmpSalaryAdmin)
admin.site.register(EmpEducation, EmpEducationAdmin)


