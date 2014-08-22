import urllib, json
from tools import *
             
def stats(bonus):
  _stats = {}
  for bs in bonus:
    if bs['stat'] in stats_used:
      _stats[stats_used[bs['stat']]] = bs['amount']
  return _stats

def do_item(data):
  return {'id':data['id'],
          'name':data['name'],
          'desc':data['nameDescription'],
          'stats':data['bstats'],
          'slot':data['inventoryType'],
          'sockets':data['hasSockets'] and data['socketInfo'],
          'icon':data['icon'],
          'quality':data['quality']}

def fetch_items(ids=[]):
  gear = []
  if not ids:
    ids = range(90000,100000)
    #ids = range(100000,111000)
  for i in ids:
    print i
    data = json.load(urllib.urlopen('https://us.api.battle.net/wow/item/%d?apikey=n3kp7varcf4wrtkmu3qcgqzszgtyznmb' % i))
    #data = json.load(urllib.urlopen('http://us.battle.net/api/wow/item/%d' % i))
    if 'status' in data:
      continue
    if data['inventoryType'] in good_inventory_slots and data['itemLevel'] >= 553:
      bstats = stats(data['bonusStats'])
      data['bstats'] = bstats
      if data['itemClass'] == 4 and data['itemSubClass'] == 3 and 'agility' in bstats: # mail agi
        gear.append(do_item(data))
      elif data['inventoryType'] in (11,2,16,15) and 'agility' in bstats: # ring, necklace, cloak, ranged
        gear.append(do_item(data))
      elif data['inventoryType'] == 12: # trinket
        gear.append(do_item(data))
  return gear