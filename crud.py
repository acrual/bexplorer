from models import db, Balances, Transactions, TransactionLists

db.create_all()
## CREATE
# (address, amount, input, block, txid, balance=0)
registro1 = Balances('dire1', 5.0, True, 70000, 'transaction1')
db.session.add(registro1)
db.session.commit()

## READ
all_puppies = Balances.query.all()
print(all_puppies)

""" ## SELECT BY ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

# FILTER will produce some SQL code for us
puppy_frankie = Puppy.query.filter_by(name = 'frankie')
print("frankie no está", puppy_frankie.all())

### UPDATE
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

## DELETE
second_puppy = Puppy.query.get(1)
db.session.delete(second_puppy)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies) """