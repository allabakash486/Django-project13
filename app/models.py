from django.db import models

# Create your models here.
class Dept(models.Model):
    Deptno = models.PositiveBigIntegerField(primary_key=True)
    Dept_name = models.CharField(max_length=20)
    Dept_loc = models.CharField(max_length=25)
    def __str__(self):
        return self.Dept_name+str(self.Deptno)
class Employees(models.Model):
    Empno = models.PositiveBigIntegerField(primary_key=True)
    Emp_name = models.CharField(max_length=25)
    comm = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    Sal = models.DecimalField(max_digits=10,decimal_places=2)
    Mgr = models.ForeignKey('self',on_delete =models.SET_NULL,null=True,blank=True)
    Dept = models.ForeignKey(Dept,on_delete=models.CASCADE)
    Hire_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Emp_name
