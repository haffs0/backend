from django.db import models

# Create your models here.
class Teachers(models.Model):
    staff_no = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    levels = models.CharField(max_length=200)
    class_held = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return self.staff_no

class Student(models.Model):
    student_no = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    student_class = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='teacher')
    
    def __str__(self):
        return self.student_no


