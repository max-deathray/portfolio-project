from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100, default="title")
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    url = models.CharField(max_length=500, default="url")

    # this allows the title of the blog to be displayed in the admin
    def __str__(self):
        return self.title
