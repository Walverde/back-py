var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://192.168.0.31:27017/ESP', function(err, db) {
  if (err) {
    throw err;
  }
  db.collection('SSS').find().toArray(function(err, result) {
    if (err) {
      throw err;
    }
    console.log(result);
  });
});