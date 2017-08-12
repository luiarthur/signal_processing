function readcsv(path) { // depends on d3
  var out = []

  d3.text(path, function(rows) {
    var data = d3.dsvFormat(" ").parseRows(rows).map(function(row) {
      return row.map(function(value) { return +value })
    })
    return out.push(data)
  })

  return out // a matrix
}

function round(x,d) {
  return +x.toFixed(d)
}

// To read a json:
//var out;
//d3.json(path, function(data) {
//    out = data
//});
