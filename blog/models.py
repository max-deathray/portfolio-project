from django.db import models


# create a blog model
class Blog(models.Model):
  # I did this part using documentation
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    # this allows the title of the blog to be displayed in the admin
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

# add the blogp app to the settings

# create a migration

# migrate

# add to the admin
