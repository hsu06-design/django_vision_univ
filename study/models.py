from django.db import models

class StudyPlan(models.Model):
    subject = models.CharField(max_length=100)
    goal = models.TextField()
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.subject
