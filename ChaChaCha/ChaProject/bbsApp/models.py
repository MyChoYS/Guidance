from django.db import models
from searchApp.models import Academy


class Academy_review(models.Model):
    password = models.CharField(max_length=8)
    content = models.CharField(max_length=500)
    academy_id = models.ForeignKey(Academy, on_delete=models.CASCADE)







# Create your models here.
