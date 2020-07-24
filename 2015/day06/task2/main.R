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
  delta = 2
  if(startsWith(line, "turn on")) {
    delta = 1
  }
  else if(startsWith(line, "turn off")) {
    delta = -1
  }
  for(x in tlx:brx) {
    for(y in tly:bry) {
      grid[x, y] = max(grid[x, y] + delta, 0)
    }
  }
}
result = sum(grid)
print(result)
