from django.db import models
from .validat import file_size

class Video(models.Model):
    video = models.FileField(upload_to="video/%y",validators=[file_size])
    video_title = models.CharField(max_length=200)
    video_description = models.CharField(max_length=200)
    price = models.PositiveIntegerField()

    def __str__(self):
        return str(self.video_title) + " ["+str(self.price)+']'

class VideoModels(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    video_title_name = models.CharField(max_length=200)
    video_description_name = models.CharField(max_length=200)
    price_name = models.PositiveIntegerField()