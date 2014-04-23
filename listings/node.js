var MongoClient = require('mongodb').MongoClient;

MongoClient.connect("mongodb://localhost:27017/exampleDb",
                    function(err, db) {
  if(err) { return console.dir(err); }

  db.collection('test',
                function(err, collection) {});
  db.collection('test',
                {strict:true},
                function(err, collection) {});

  db.createCollection('test', {w:1}, function(err, collection) {
    collection.insert(doc2, {w:1}, function(err, result) {
      collection.update(
        { mykey: 2 },
        { $push: {
            docs: {doc2:1}
        } },
        {w:1},
        function(err, result) {});
    });
  });
});
