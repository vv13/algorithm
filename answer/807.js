/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxIncreaseKeepingSkyline = function(grid) {
  const len = grid.length;
  const horizon = [];
  const veritcle = [];
  for (let i = 0; i < len; i++) {
    let hMax = 0;
    grid[i].forEach(e => {
      if (e > hMax) {
        hMax = e;
      }
    });
    horizon.push(hMax);

    let vMax = 0;
    grid.forEach(e => {
      if (e[i] > vMax) {
        vMax = e[i];
      }
    });
    veritcle.push(vMax);
  }
  let increase = 0;
  for (let x = 0; x < len; x++) {
    for (let y = 0; y < len; y++) {
      increase += Math.min(horizon[x], veritcle[y]) - grid[y][x];
    }
  }
  return increase;
};
