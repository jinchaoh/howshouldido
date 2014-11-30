from django.db import models

<<<<<<< HEAD
# Create your models here.
=======

# Create your models here.
class Step(models.Model):
    content = models.TextField();
    pic = models.ImageField(upload_to = 'templates/photos/');
    
class Blog(models.Model):
    title = models.CharField(max_length = 200,blank = False)
    author = models.CharField(max_length = 100,blank = False)
    datetime = models.DateTimeField()
    helpful = models.Count()
    unhelpful = models.Count()
    step = models.ForeignKey(Step)
    
    
    
>>>>>>> refs/remotes/origin/integrate
