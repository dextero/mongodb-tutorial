// przyklad: znajdz osoby w wieku miedzy 20 a 40 lat lub takie, ktorych imie konczy sie na a
db.users.find({ $or: [ { age: { $gt: 20, $lt: 40 } },
                       { name: /.*a$/ } ] })
