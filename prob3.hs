import Data.List
import Data.Maybe

main :: IO ()
main = print problem_3
num = 13195

factors n = [x | x <- [2..n], n `mod` x == 0]

is_prime n = if factors n == [1,n] then True else False
smallest_divisor n = head (factors n)

largest_prime_factor n = maximum [x | x <- (factors n), is_prime x]
problem_3 = largest_prime_factor num


prime_factors n
  |  n `div` x ==1 = x:[]
  | otherwise = x: prime_factors (n `div` x)
  where
    x = smallest_divisor n
