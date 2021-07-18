from django.db import models

# Create your models here.


class Submission(models.Model):
    question_id = models.IntegerField()
    name = models.CharField(default="", max_length=100)
    code = models.TextField()
    verdict = models.CharField(max_length=12)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.question_id)


class Question(models.Model):
    question_id = models.IntegerField()
    text = models.TextField()
    input = models.TextField(default="")
    output = models.TextField(default="")
    name = models.CharField(default="", max_length=100)
    topics = models.CharField(default="", max_length=100)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.question_id)
