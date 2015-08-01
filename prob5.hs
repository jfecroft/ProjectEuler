import Data.List
main :: IO ()
main = print output 
problem_5 :: Maybe Int


isMultiple :: Int -> Int -> Bool
isMultiple y x = all (==True) [(== 0) $ mod x i |i <-[1..y]]
problem_5 = findIndex (isMultiple 20) [1..]
output :: Int
output = case problem_5 of
        Just x -> x + 1
        Nothing -> 0 
