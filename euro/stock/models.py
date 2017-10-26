from django.db import models




   
class products(models.Model):
   name=models.CharField(max_length=200)
   specs=models.TextField()
   stocks=models.CharField(max_length=200)
   pub_date=models.DateTimeField('date published') 
   image1=models.ImageField(upload_to="images/media/")
   def __unicode__(self):
     return self.name
    
