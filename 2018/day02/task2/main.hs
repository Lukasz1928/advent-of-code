import System.IO

countDifferentPostions :: String ->String -> Int
countDifferentPostions s1 s2 = (length s1) - (length $ filter (==True) $ zipWith (==) s1 s2)

calculateCommonPart :: String -> String -> String
calculateCommonPart s1 s2 = map(\(x, y) -> x) $ filter (\(x, y) -> x == y) $ zip s1 s2

main = do
    handle <- openFile "input" ReadMode
    contents <- hGetContents handle
    let ids = lines contents
    let pairs = [(x, y) | x <- ids, y <- ids]
    let dif = head $ filter (\(x, y) -> countDifferentPostions x y == 1) pairs
    let result = calculateCommonPart (fst dif) (snd dif)
    putStrLn result
    hClose handle
