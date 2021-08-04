{-
  Haskell 99 Problems 11-20 Solving
-}

-- Problem 11
-- Modified run-length encoding.
-- Modify the result of problem 10 in such a way that
-- if an element has no duplicates it is simply copied
-- into the result list. Only elements with duplicates
-- are transferred as (N E) lists.

data EncodingList a = Single a | Multiple Int a deriving (Show)

encodeModified :: Eq a => [a] -> [EncodingList a]
encodeModified = map encodeHelper . encode 
  where
    encodeHelper (1,x) = Single x 
    encodeHelper (n,x) = Multiple n x

-- Problen 12
-- Decode a run-length encoded list.
-- Given a run-length code list generated as
-- specified in problem 11. Construct its uncompressed version.
decodeModified :: [EncodingList a] -> [a]
decodeModified = concatMap decodeHelper
  where
    decodeHelper (Single x) = [x]
    decodeHelper (Multiple n x) = replicate n x

-- Problem 13
-- Run-length encoding of a list (direct solution).
-- Implement the so-called run-length encoding data
-- compression method directly. I.e. don't explicitly
-- create the sublists containing the duplicates,
-- as in problem 9, but only count them. As in problem P11,
-- simplify the result list by replacing the singleton
-- lists (1 X) by X.

-- Problem 14
-- Duplicate the elements of a list.
dupli :: [a] -> [a]
dupli = concatMap (replicate 2) 

-- Problem 15
-- Replicate the elements of a list a given number of times.
repli :: [a] -> Int -> [a]
repli xs n = concatMap (replicate n) xs

-- Problem 16
-- Drop every N'th element from a list.
dropEvery :: [a] -> Int -> [a]
dropEvery xs n = map fst $ filter ((n/=) . snd) $ zip xs [1..]

-- Problem 17
-- Split a list into two parts; the length of the first part is given.
-- Do not use any predefined predicates.

-- Problem 18
-- Extract a slice from a list.
-- Given two indices, i and k, the slice is the list
-- containing the elements between the i'th and k'th element
-- of the original list (both limits included).
-- Start counting the elements with 1.
slice :: [a] -> Int -> Int -> [a]
slice xs n n' = take (n'-n+1) $ drop (n-1) xs 

-- Problem 19
-- Rotate a list N places to the left.
-- Hint: Use the predefined functions length and (++).
rotate :: [a] -> Int -> [a]
rotate xs n | n >= 0 = drop n xs ++ take n xs
            | n < 0 = drop len xs ++ take len xs
                      where len = n+length xs

rotate' xs n = drop n' xs ++ take n' xs 
  where n' = n `mod` length xs

-- Problem 20
-- Remove the K'th element from a list.
removeAt :: Int -> [a] -> (a, [a])
removeAt n xs = (xs!!(n-1) , take (n-1) xs ++ drop n xs)