function makePiano(tag) {
  var svgPiano = d3.select(tag)

  var numWhiteKeys = 52
  var whiteKeyHeight = +svgPiano.attr("height")
  var whiteKeyWidth = +svgPiano.attr("width") / numWhiteKeys

  var blackKeyHeight =  +svgPiano.attr("height") *.7
  var blackKeyWidth =  +svgPiano.attr("width") / numWhiteKeys / 2

  var letterNames = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
  var numLetters = letterNames.length
  var sharpableNotes = ['C', 'D', 'F', 'G', 'A']

  function makeBlacKey(i, whiteName, octave) {
    if (sharpableNotes.indexOf(whiteName) > -1 & whiteName+octave != 'C8') {
      var letterName = whiteName + 's';
      function annotate(x) { return "key-" + x + " " }
      svgPiano.append("rect")
              .attr("x", i * whiteKeyWidth + whiteKeyWidth - blackKeyWidth/2 )
              .attr("y", 0)
              .attr("width", blackKeyWidth)
              .attr("height", blackKeyHeight)
              .attr("class", ["black", letterName, "octave"+octave].map(annotate).join(' '))
    }
  }

  function makeWhiteKey(i) {
    var letterName = letterNames[ i % numLetters ];
    var octave = i > 1 ? Math.floor((i+numLetters-2) / numLetters) : 0
    function annotate(x) {return "key-" + x + " " }

    svgPiano.append("rect")
            .attr("x", i * whiteKeyWidth)
            .attr("y", 0)
            .attr("width", whiteKeyWidth)
            .attr("height", whiteKeyHeight)
            .attr("class", ["white", letterName, "octave"+octave].map(annotate).join(' '))

    makeBlacKey(i, letterName, octave)
  }
  for (i=0; i<numWhiteKeys; i++) { makeWhiteKey(i) }
}
