db.users.find()
db.users.find({ name: 'Andrzej' })
db.users.find({ age: { $le: 30 } })
