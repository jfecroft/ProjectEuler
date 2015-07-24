main :: IO ()
main = print problem_14
problem_14 = snd $ maximum ( zip [length $ collatz(i)| i <- [1..1000000]] [1..])

collatz :: Integer -> [Integer]
collatz 1 = [1]
collatz n
    | even n = n: collatz (n `div` 2)
    | odd n = n:collatz (n*3 + 1)
