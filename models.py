from django.db import models
from tools import slots

socket_choices=[('red','Red'),
                ('yellow','Yellow'),
                ('blue','Blue'),
                ('meta','Meta'),
                ('chromatic','Chromatic'),
                ('none','(No socket)'),
                   ]

# Create your models here.
class GearItem(models.Model):
    name = models.CharField(max_length=80)
    nameDescription = models.CharField(max_length=80,blank=True)
    zone = models.CharField(max_length=80)
    source = models.CharField(max_length=80)
    agility = models.IntegerField(default=0)
    crit = models.IntegerField(default=0)
    haste = models.IntegerField(default=0)
    mastery = models.IntegerField(default=0)
    multistrike = models.IntegerField(default=0)
    versatility = models.IntegerField(default=0)
    ilvl = models.IntegerField(default=0)
    icon = models.CharField(max_length=80)
    slot = models.IntegerField(default=0)
    quality = models.IntegerField(default=0)
    socket1 = models.CharField(max_length=20,blank=True,
                               choices=socket_choices,)
    socket2 = models.CharField(max_length=20,blank=True,
                               choices=socket_choices,)
    socket3 = models.CharField(max_length=20,blank=True,
                               choices=socket_choices,)
    socket_bonus = models.CharField(max_length=80,blank=True)
    
    def slotName(self):
      return slots[self.slot]

    def __unicode__(self):
       return self.name + ' (' + (self.nameDescription or 'normal') + ')'