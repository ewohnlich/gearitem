from django.db import models

class Comment(models.Model):
    gearid = models.CharField(max_length=80)
    user = models.CharField(max_length=80)
    note = models.TextField()

    def __unicode__(self):
       return self.user + ': ' + self.note[:20]

# Create your models here.
class GearItem(models.Model):
    name = models.CharField(max_length=80)
    zone = models.CharField(max_length=80)
    source = models.CharField(max_length=80)
    primary = models.IntegerField(default=0)
    crit = models.IntegerField(default=0)
    haste = models.IntegerField(default=0)
    mastery = models.IntegerField(default=0)
    
    def comments(self):
      return Comment.objects.filter(gearid=self.id)

    def __unicode__(self):
       return self.name