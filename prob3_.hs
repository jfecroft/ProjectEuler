import Data.List
import Data.Maybe

main :: IO ()
main = print problem_3
num = 13195

factors n = [x | x <- [1..n], n `mod` x == 0]

is_prime n = if factors n == [1,n] then True else False

largest_prime_factor n = maximum [x | x <- (factors n), is_prime x]
problem_3 = largest_prime_factor num

is_divisor x y = (x `mod` y) == 0
smallest_divisor n = fromJust (find (is_divisor n) [2..n])

factors' n = x: factors' (n `div` x)
  where
    x = smallest_divisor n
