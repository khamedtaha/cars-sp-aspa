from django.db import models




class Video(models.Model):
      name=models.CharField(max_length=100)
      video=models.FileField(upload_to="video/")
      def __str__(self):
         return self.name
      
      def delete(self ,*args, **kwargs) : 
         self.video.delete(save=False)
         super().delete(*args, **kwargs) 
