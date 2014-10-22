import urllib, json
from tools import *
from calcs.tools import API_KEY
             
def stats(bonus):
  _stats = {}
  for bs in bonus:
    if bs['stat'] in stats_used:
      _stats[stats_used[bs['stat']]] = bs['amount']
  return _stats

def do_item(data):
  val = {'id':data['id'],
          'name':data['name'],
          'ilvl':data['itemLevel'],
          'desc':data['nameDescription'],
          'stats':data['bstats'],
          'slot':data['inventoryType'],
          'sockets':data['hasSockets'] and data['socketInfo'],
          'icon':data['icon'],
          'quality':data['quality'],}
  if 'weaponInfo' in data:
    val['weapon_min'] = data['weaponInfo']['damage']['exactMin']
    val['weapon_max'] = data['weaponInfo']['damage']['exactMax']
    val['weapon_speed'] = data['weaponInfo']['weaponSpeed']
  return val

def fetch_items(ids=[]):
  import time
  gear = []
  if not ids:
    ids = range(105847,111000)
  for i in ids:
    #time.sleep(1) # we should really only sleep if it hits the limit, then retry
    data = json.load(urllib.urlopen('https://us.api.battle.net/wow/item/%d?apikey=%s' % (i,API_KEY)))
    if 'status' in data:
      continue
    if 'inventoryType' not in data and 'availableContexts' in data:
      if 'raid-normal' in data['availableContexts']:
        data = json.load(urllib.urlopen('https://us.api.battle.net/wow/item/%d/raid-normal?apikey=%s' % (i,API_KEY)))
      else:
        context = data['availableContexts'][0]
        data = json.load(urllib.urlopen('https://us.api.battle.net/wow/item/%d/%s?apikey=%s' % (i,context,API_KEY)))
    if data['inventoryType'] in good_inventory_slots:
      bstats = stats(data['bonusStats'])
      data['bstats'] = bstats
      if data['itemClass'] == 4 and data['itemSubClass'] == 3 and 'agility' in bstats: # mail agi
        gear.append(do_item(data))
      elif data['inventoryType'] in (11,2,16,15,26) and 'agility' in bstats: # ring, necklace, cloak, ranged
        gear.append(do_item(data))
      elif data['inventoryType'] == 12: # trinket
        gear.append(do_item(data))
  return gear