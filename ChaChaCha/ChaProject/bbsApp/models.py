from django.db import models
from searchApp.models import Academy,TestSite

class Academy_review(models.Model):
    password = models.CharField(max_length=8)
    content = models.CharField(max_length=500)
    academy_id = models.ForeignKey(Academy, on_delete=models.CASCADE)


class TestSite_review(models.Model):
    password = models.CharField(max_length=8)
    content = models.CharField(max_length=500)
    testsite_id = models.ForeignKey(TestSite, on_delete=models.CASCADE)

