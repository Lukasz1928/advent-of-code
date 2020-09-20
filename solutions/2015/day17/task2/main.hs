import System.IO

findMinimalNumberOfContainersAgg :: [Int] -> Int -> Int -> Int
findMinimalNumberOfContainersAgg sizes 0 agg = agg
findMinimalNumberOfContainersAgg [] total agg = if total == 0 then agg else maxBound :: Int
findMinimalNumberOfContainersAgg sizes total agg = min (findMinimalNumberOfContainersAgg (tail sizes) (total - sizes!!0) (agg + 1)) (findMinimalNumberOfContainersAgg (tail sizes) total agg)

findMinimalNumberOfContainers :: [Int] -> Int -> Int
findMinimalNumberOfContainers sizes total = findMinimalNumberOfContainersAgg sizes total 0

countContainerCombinations :: [Int] -> Int -> Int -> Int
countContainerCombinations sizes 0 number = if number == 0 then 1 else 0
countContainerCombinations [] total number = if total == 0 && number == 0 then 1 else 0
countContainerCombinations sizes total number = countContainerCombinations (tail sizes) (total - sizes!!0) (number - 1) + countContainerCombinations (tail sizes) total number

main = do
    handle <- openFile "input" ReadMode
    contents <- hGetContents handle
    let sizes = map (\x -> read x :: Int) (lines contents)
    let eggnogAmount = 150
    
    let minContainers = findMinimalNumberOfContainers sizes eggnogAmount
    let result = countContainerCombinations sizes eggnogAmount minContainers
    putStrLn $ show result
    
    hClose handle
