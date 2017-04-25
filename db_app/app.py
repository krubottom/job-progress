from tinydb import TinyDB, Query

db = TinyDB('db.json')

# db.insert({'name': 'd1', 'type': 'door', 'dc': 'False', 'rex': 'False'})

item = Query()

print db.search(item.type == 'door')
