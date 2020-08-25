from django.db import models


class Post(models.Model):
    boast = models.BooleanField()
    content = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0, null=True, blank=True)
    downvotes = models.IntegerField(default=0, null=True, blank=True)
    submission_time = models.DateTimeField(auto_now_add=True)

    def score(self):
        return self.upvotes - self.downvotes
