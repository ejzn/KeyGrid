import web

db = web.database(dbn='mysql', host='127.0.0.1', db='keygrid', user='plana', pw='plana')

def get_keys():
    return db.select('key', order='id')

def new_key(text, assignee, location, unit, status):
    db.insert('key', code=text, assignee=assignee, location=location, unit=unit, status=status)

def del_key(id):
    db.delete('key', where="id=$id", vars=locals())

def get_locations():
    return db.select('location', order='id')

def new_location(name, address, manager):
    db.insert('location', name=name, address=address, manager=manager)

def del_location(id):
    db.delete('location', where="id=$id", vars=locals())

def get_units():
    return db.select('unit', order='id')

def new_unit(number):
    db.insert('unit', number=number)

def del_unit(id):
    db.delete('unit', where="id=$id", vars=locals())





