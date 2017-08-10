main :: IO ()
main = print problem_3
num = 600851475143

factors n = [x | x <- [2..n], n `mod` x == 0]

smallest_divisor n = head (factors n)

prime_factors n
  |  n `div` x ==1 = x:[]
  | otherwise = x: prime_factors (n `div` x)
  where
    x = smallest_divisor n

problem_3 = last (prime_factors num)
