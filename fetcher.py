import urllib, json, os, time
from django.core.exceptions import ObjectDoesNotExist

from tools import *
from calcs.tools import API_KEY
from models import GearContext, GearItem

def stats(bonus):
  _stats = {}
  for bs in bonus:
    if bs['stat'] in stats_used:
      _stats[stats_used[bs['stat']]] = bs['amount']
  return _stats

def do_item(data):
  val = {'id':data.get('id'),
          'name':data.get('name'),
          'ilvl':data.get('itemLevel'),
          'desc':data.get('nameDescription'),
          'stats':data.get('bstats'),
          'slot':data.get('inventoryType'),
          'icon':data.get('icon'),
          'quality':data.get('quality'),}
  if 'weaponInfo' in data:
    val['weapon_min'] = data['weaponInfo']['damage']['exactMin']
    val['weapon_max'] = data['weaponInfo']['damage']['exactMax']
    val['weapon_speed'] = data['weaponInfo']['weaponSpeed']

  if not val['stats']:
    _stats = {}
    for stat in data.get('bonusStats'):
      if stat['stat'] in stats_used:
        stat_name = stats_used[ stat['stat'] ]
        _stats[stat_name] = stat['amount']

    val['stats'] = _stats
  return val

def update_gear(gear,fromcontext=False):
  print 'Updating item: %d' % gear['id']
  try:
    obj = GearItem.objects.get(id=gear['id'])
  except ObjectDoesNotExist:
    obj = GearItem.objects.create(id=gear['id'])
  if obj.name and obj.name != gear['name']:
    print 'Warning: %d renamed from %s to %s' % (gear['id'],obj.name,gear['name'])
  obj.name = gear['name']
  obj.nameDescription = not fromcontext and gear['desc'] or ''
  obj.agility = not fromcontext and gear['stats'].get('agility',0) or 0
  obj.crit = not fromcontext and gear['stats'].get('crit',0) or 0
  obj.haste = not fromcontext and gear['stats'].get('haste',0) or 0
  obj.mastery = not fromcontext and gear['stats'].get('mastery',0) or 0
  obj.versatility = not fromcontext and gear['stats'].get('versatility',0) or 0
  obj.multistrike = not fromcontext and gear['stats'].get('multistrike',0) or 0
  obj.weapon_min = not fromcontext and gear.get('weapon_min',0)
  obj.weapon_max = not fromcontext and gear.get('weapon_max',0)
  obj.weapon_speed = not fromcontext and gear.get('weapon_speed',0)
  if gear['ilvl']:
    obj.ilvl = gear['ilvl']
  obj.icon = gear['icon'] or ''
  obj.slot = gear['slot']
  obj.quality = gear['quality']
  obj.save()
  obj.ilvl = obj.maxIlvl
  obj.save()

def update_context(context,data):
  data = do_item(data)
  context.agility = data['stats'].get('agility',0)
  context.crit = data['stats'].get('crit',0)
  context.haste = data['stats'].get('haste',0)
  context.mastery = data['stats'].get('mastery',0)
  context.versatility = data['stats'].get('versatility',0)
  context.multistrike = data['stats'].get('multistrike',0)
  context.weapon_min = data.get('weapon_min',0)
  context.weapon_max = data.get('weapon_max',0)
  context.weapon_speed = data.get('weapon_speed',0)
  context.ilvl = data.get('ilvl')
  context.save()

  for bonus in data.get('bonusChances',[]):
    pass

def scrub_contexts(data):
  return [cd for cd in data['availableContexts'] if cd]

def fetch_items(ids=[]):
  BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)),'gearitem')
  f=open(os.path.join(BASE_DIR,'ignore.json'))
  ignore = json.load(f); f.close()
  gear = []
  if not ids:
    ids = range(100000,130000)
    # don't worry about ones we already have yet
    ids = [i for i in ids if i not in GearItem.objects.all().values_list('id',flat=True)]
  ids = [i for i in ids if i not in ignore]

  for i in ids:
    #time.sleep(1) # we should really only sleep if it hits the limit, then retry
    data = json.load(urllib.urlopen('https://us.api.battle.net/wow/item/%d?apikey=%s' % (i,API_KEY)))
    if 'status' in data and ('page not found' in data['reason'] or 'unable to get' in data['reason']): # invalid item
      print 'not found: %d' % i
      ignore.append(i)
      continue
    elif 'status' in data:
      time.sleep(1)
      data = json.load(urllib.urlopen('https://us.api.battle.net/wow/item/%d?apikey=%s' % (i,API_KEY)))
      if 'status' in data:
        raise Exception('bad status')
    if 'availableContexts' in data and bool(scrub_contexts(data)):
      isrelevant = True # if a context is not an agi item don't get anything
      for context in data['availableContexts']:
        if not isrelevant:
          continue
        cdata = json.load(urllib.urlopen('https://us.api.battle.net/wow/item/%d/%s?apikey=%s' % (i,context,API_KEY)))

        # create the GearItem if it does not exist
        try:
          _gear = GearItem.objects.get(id=i)
        except GearItem.DoesNotExist:
          # check if it's a valid item first
          context = data['availableContexts'][0]
          data = json.load(urllib.urlopen('https://us.api.battle.net/wow/item/%d/%s?apikey=%s' % (i,context,API_KEY)))
          bstats = stats(data.get('bonusStats',[]))

          mailagi = data['itemClass'] == 4 and data['itemSubClass'] == 3 and 'agility' in bstats
          nonarmoragi = data['inventoryType'] in (11,2,16,15,26) and 'agility' in bstats
          istrinket = data['inventoryType'] == 12
          if (mailagi or nonarmoragi or istrinket) and data['quality'] > 2: # no more greens
            GearItem.objects.create(id=i)
            _gear = GearItem.objects.get(id=i)
          else:
            isrelevant = False

        if isrelevant:
          contexts = []
          # create the contexts if they don't exist
          try:
            cobj = GearContext.objects.get(context=context,gearitem_id=i)
            update_context(cobj,cdata)
          except GearContext.DoesNotExist:
            cobj = GearContext.objects.create(gearitem=_gear,context=context)
            cobj.save()
            update_context(cobj,cdata)
            contexts.append(cdata)

      # set the regular stuff
      if isrelevant:
        context = data['availableContexts'][-1]
        data = json.load(urllib.urlopen('https://us.api.battle.net/wow/item/%d/%s?apikey=%s' % (i,context,API_KEY)))
        update_gear(do_item(data),fromcontext=True)

    else: # old style or not gear

      if 'inventoryType' in data and data['inventoryType'] in good_inventory_slots and data['itemLevel'] >= 540 and data['quality'] > 2:
        bstats = stats(data.get('bonusStats',[]))
        data['bstats'] = bstats
        if data['itemClass'] == 4 and data['itemSubClass'] == 3 and 'agility' in bstats: # mail agi
          update_gear(do_item(data))
        elif data['inventoryType'] in (11,2,16,15,26) and 'agility' in bstats: # ring, necklace, cloak, ranged
          update_gear(do_item(data))
        elif data['inventoryType'] == 12: # trinket
          update_gear(do_item(data))
        else:
          ignore.append(i)
          print 'not gear: %d' % i
  f=open(os.path.join(BASE_DIR,'ignore.json'),'w')
  json.dump(ignore,f); f.close()