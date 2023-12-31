from django.db import models

# Create your models here.
class Book(models.Model):
  name=models.CharField(max_length=50)
  author=models.CharField(max_length=50)
  email=models.EmailField(blank=True)
  summary=models.TextField()
  def __str__(self) -> str:
    return self.name + '; Author:' + self.author