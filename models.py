from django.db import models
from tools import slots

socket_choices=[('red','Red'),
                ('yellow','Yellow'),
                ('blue','Blue'),
                ('meta','Meta'),
                ('chromatic','Chromatic'),
                ('none','(No socket)'),
                   ]

slot_choices = [(15,"Weapon"),
                (1,"Head"),
                (2,"Neck"),
                (3,"Shoulder"),
                (16,"Cloak"),
                (5,"Chest"),
                (6,"Waist"),
                (7,"Legs"),
                (8,"Feet"),
                (9,"Wrist"),
                (10,"Hands"),
                (11,"Finger"),
                (12,"Trinket"),
                (20,"Chest (gown)")]
quality_choices = [(3,"Superior"),
                   (4,"Epic"),
                   (5,"Legendary")]

# Create your models here.
class GearItem(models.Model):
    id = models.IntegerField(primary_key=True)
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
    weapon_min = models.FloatField(default=0)
    weapon_max = models.FloatField(default=0)
    weapon_speed = models.FloatField(default=0)
    ilvl = models.IntegerField(default=0)
    icon = models.CharField(max_length=80,default="inv_misc_questionmark")
    slot = models.IntegerField(default=0,choices=slot_choices)
    quality = models.IntegerField(default=0,choices=quality_choices)
    socket1 = models.CharField(max_length=20,blank=True,
                               choices=socket_choices,)
    socket2 = models.CharField(max_length=20,blank=True,
                               choices=socket_choices,)
    socket3 = models.CharField(max_length=20,blank=True,
                               choices=socket_choices,)
    socket_bonus = models.CharField(max_length=80,blank=True)
    
    def slotName(self):
      return slots[self.slot]
    
    def maxIlvl(self):
      if hasattr(self,'gearcontext_set') and self.gearcontext_set.all():
        return self.gearcontext_set.all().aggregate(models.Max('ilvl'))['ilvl__max']
      return self.ilvl

    def __unicode__(self):
      return (self.nameDescription and 'Season' not in self.nameDescription) and self.name + ' (' + (self.nameDescription) + ')' or self.name
    
    class Meta:
      ordering = ['-ilvl','name']

class Gem(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    agility = models.IntegerField(default=0,blank=True)
    crit = models.IntegerField(default=0,blank=True)
    haste = models.IntegerField(default=0,blank=True)
    mastery = models.IntegerField(default=0,blank=True)
    multistrike = models.IntegerField(default=0,blank=True)
    versatility = models.IntegerField(default=0,blank=True)

    def __unicode__(self):
      return self.name

class GearContext(models.Model):
    gearitem = models.ForeignKey('GearItem')
    context = models.CharField(max_length=80)
    agility = models.IntegerField(default=0,blank=True)
    crit = models.IntegerField(default=0,blank=True)
    haste = models.IntegerField(default=0,blank=True)
    mastery = models.IntegerField(default=0,blank=True)
    multistrike = models.IntegerField(default=0,blank=True)
    versatility = models.IntegerField(default=0,blank=True)
    weapon_min = models.FloatField(default=0)
    weapon_max = models.FloatField(default=0)
    weapon_speed = models.FloatField(default=0)
    warforged_agility = models.IntegerField(default=0,blank=True)
    warforged_crit = models.IntegerField(default=0,blank=True)
    warforged_haste = models.IntegerField(default=0,blank=True)
    warforged_mastery = models.IntegerField(default=0,blank=True)
    warforged_multistrike = models.IntegerField(default=0,blank=True)
    warforged_versatility = models.IntegerField(default=0,blank=True)
    warforged_weapon_min = models.FloatField(default=0)
    warforged_weapon_max = models.FloatField(default=0)
    warforged_weapon_speed = models.FloatField(default=0)
    ilvl = models.IntegerField(default=0)
    warforged_ilvl = models.IntegerField(default=0)
    
    def contextPretty(self):
      return u' '.join([cp == 'pvp' and cp.upper() or len(cp)>1 and cp[0].upper()+cp[1:] or cp for cp in self.context.split('-')])

    def __unicode__(self):
      return '%s - %s' % (self.gearitem.name, self.context)