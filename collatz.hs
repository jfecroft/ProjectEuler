main :: IO ()
main = print problem
problem = collatz(9)
collatz :: Integer -> [Integer]
collatz 1 = [1]
collatz n
    | even n = n: collatz (n `div` 2)
    | odd n = n:collatz (n*3 + 1)
