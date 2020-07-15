from django.db import models


# Create your models here.
class Query(models.Model):
    type = (
        ('Programming', 'Programming'),
        ('Math', 'Math'),
        ('Science', 'Science'),
        ('English', 'English'),
        ('Others', 'Others'),
    )
    title = models.CharField(max_length=150)
    question_type = models.CharField(default=1, choices=type, max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='pictures/', default='pctures/None/no-img.jpg')

    def __str__(self):
        return self.title
