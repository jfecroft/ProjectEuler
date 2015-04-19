main :: IO ()
main = print problem_1 
problem_1 :: Integer
problem_1 = sum [x |x <- [0..1000-1] ,(x `mod` 3 == 0) || (x `mod` 5 == 0)]
