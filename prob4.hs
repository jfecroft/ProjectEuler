import Data.List
main :: IO ()
main = print problem_3

problem_3 :: Integer
problem_3 = last $  sort [read x  :: Integer |  x<- [show $ i*j| i <- [100..999],j <- [100..999], reverse(show(i*j)) == show(i*j)]]
