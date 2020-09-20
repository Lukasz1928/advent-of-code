import System.IO

countCombinationsWithTotal :: [Int] -> Int -> Int
countCombinationsWithTotal [] total = if total == 0 then 1 else 0
countCombinationsWithTotal sizes total = if total >= 0 then countCombinationsWithTotal (tail sizes) (total - sizes!!0) + countCombinationsWithTotal (tail sizes) total else 0

main = do
    handle <- openFile "input" ReadMode
    contents <- hGetContents handle
    let sizes = map (\x -> read x :: Int) (lines contents)
    let eggnogAmount = 150
    
    let result = countCombinationsWithTotal sizes eggnogAmount
    putStrLn $ show result
    
    hClose handle
