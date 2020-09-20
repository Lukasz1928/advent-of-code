readInput = function() {
  f = file("input", "r")
  lines = readLines(f)
  close(f)
  return(lines)
}

input = readInput()

grid = matrix(0, 1000, 1000)
for(line in input) {
  coords = str_extract_all(line, "\\d+")
  tlx = strtoi(coords[[1]][[1]]) + 1
  tly = strtoi(coords[[1]][[2]]) + 1
  brx = strtoi(coords[[1]][[3]]) + 1
  bry = strtoi(coords[[1]][[4]]) + 1
  if(startsWith(line, "turn on")) {
    grid[tlx:brx, tly:bry] = 1
  }
  else if(startsWith(line, "turn off")) {
    grid[tlx:brx, tly:bry] = 0
  }
  else {
    for(x in tlx:brx) {
      for(y in tly:bry) {
        grid[x, y] = 1 - grid[x, y]
      }
    }
  }
}
result = sum(grid)
print(result)
