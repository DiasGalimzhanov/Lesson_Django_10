from django.db import models
from django.db.models import F, Q

class CustomUser(models.Model):
    class GenderChoices(models.TextChoices):
        F = 'F', 'Female'
        M = 'M', 'Male'
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GenderChoices.choices)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        

class Todo(models.Model):
    class TodoStatus(models.TextChoices):
        C = 'C', 'Created'
        P = 'P', 'Processed'
        D = 'D', 'Done'
        
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=TodoStatus.choices,default=TodoStatus.C)
    deadline = models.DateField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='todos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
