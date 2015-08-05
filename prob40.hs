import Data.Char
import Data.List

main :: IO ()
main = print output 
d :: Int -> Int
d x = digitToInt $ concat [show y | y <- [1..]] !! (x - 1)
output :: Int
output = product [d $ 10^x | x <- [0..6]]
