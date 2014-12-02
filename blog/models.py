from django.db import models

# Create your models here.
class Step(models.Model):
    num = models.IntegerField()
    content = models.TextField()
    pic = models.ImageField(upload_to = 'templates/photos/')
    
    def __unicode__(self):
        return self.id
    
class Blog(models.Model):
    title = models.CharField(max_length = 200,blank = False)
    author = models.CharField(max_length = 100,blank = False)
    datetime = models.DateTimeField(auto_now = True)
    helpful = models.IntegerField()
    unhelpful = models.IntegerField()
    step = models.ForeignKey(Step)
    
    def __unicode__(self):
        return self.title
    

