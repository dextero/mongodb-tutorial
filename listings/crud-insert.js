db.users.insert({ name: 'Andrzej', age: 26 })
db.users.insert([ { name: 'Barbara', age: 10 },
                  { name: 'Cecylia', age: 40 } ])

db.users.update({ name: 'Dariusz' },
                { $set: { age: 37 } },
                { upsert: true })

db.users.save({ name: 'Eugeniusz', age: 63 })
