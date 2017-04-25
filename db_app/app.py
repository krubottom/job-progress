from tinydb import TinyDB, Query

db = TinyDB('db.json')

# db.insert({'name': 'd1', 'type': 'door', 'dc': 'False', 'rex': 'False', 'dc-input': 'uri0-1'})

item = Query()

print db.search(item.type == 'door')
