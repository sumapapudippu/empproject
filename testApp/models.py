from django.db import models

class Employee(models.Model):
	eno=models.CharField(max_length=10)
	ename=models.CharField(max_length=30)
	esal=models.FloatField()
	eaddr=models.CharField(max_length=30)
	def __str__(self):
		return self.ename


