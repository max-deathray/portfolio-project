from django.db import models


# create a blog model
class Blog(models.Model):
  # I did this part using documentation
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# add the blogp app to the settings

# create a migration

# migrate

# add to the admin
