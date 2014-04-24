db.products.insert(
  (function () {
    function randint(max) {
      return ~~(Math.random()*max);
    }

    function chooseRandom(arr) {
      return arr[randint(arr.length)];
    }

    function generateName() {
      var minLength = 1;
      var maxLength = 3;
      var length = minLength + randint(maxLength - minLength);

      var name = '';

      for (var i = 0; i < length; ++i) {
        name += String.fromCharCode('a'.charCodeAt(0) + randint('z'.charCodeAt(0) - 'a'.charCodeAt(0) + 1));
      }
      return name;
    }

    function generateArray(generator, n) {
      var arr = [];
      for (var i = 0; i < n; ++i) {
        arr.push(generator());
      }
      return arr
    }

    var names = generateArray(generateName, 100);
    var features = generateArray(generateName, 100);

    function generateFeature() {
      var feature = {};
      feature[chooseRandom(features)] = randint(100);
      return feature;
    }

    function generateProduct() {
      return {
        name: chooseRandom(names),
        price: randint(10000),
        features: generateArray(generateFeature, randint(5))
      };
    }

    return generateArray(generateProduct, 100000);
  })()
)

db.products.find({
  features: {
    $elemMatch: {
      a: { $exists: 1 }
    }
  }
}, {
  name: 1,
  features: 1,
  _id: 0
})


