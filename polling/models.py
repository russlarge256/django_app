from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title
