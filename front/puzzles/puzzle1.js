var puzzle_array = [{a4: 'bK', c4: 'wK', a6: 'wR'}, 
                    {a2: 'wR', c2: 'wR', e1: 'wK', g3: 'bP',
                     h3: 'bQ', h4: 'bK'},
                    {a8: 'wK', d8: 'wB', f8: 'bK', e6: 'wB'} ];

function nextPuzzle() {
  counter += 1;
  if(counter >= puzzle_array.length) {
    counter = 0;
  }
  board2.position(puzzle_array[counter]);
}
