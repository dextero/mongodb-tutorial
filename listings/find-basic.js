db.users.find({ $or: [ { age: { $gt: 20, $lt: 40 } },
                       { name: /.*a/ } ] })
