from django.db import models

class Image(models.Model):
    picture = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=200, default="picture")
    first_name = models.CharField(max_length=20, default="")
    second_name = models.CharField(max_length=20, default="")
    first_value = models.FloatField(default=0)
    second_value = models.FloatField(default=0)
    

    def __str__(self):
        return self.title
