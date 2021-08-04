{-
  Haskell 99 Problems 1-10 Solving
-}

-- Problem 1
-- Find the last element of a list.
myLast :: [a] -> a
myLast []     = error "empty list"
myLast [x]    = x
myLast (_:xs) = myLast xs

myLast' = head . reverse

-- Problem 2
-- Find the last but one element of a list.
myButLast :: [a] -> a
myButLast = last . init

myButLast' = head . drop 1 . reverse -- like myLast'

myButLast'' [x,_] = x
myButLast'' (_:xs) = myButLast'' xs

-- Problem 3
-- Find the K'th element of a list.
-- The first element in the list is number 1.
elementAt :: [a] -> Int -> a
elementAt xs n = xs !! (n - 1)

-- Problem 4
myLength :: [a] -> Int
myLength xs = sum [ 1 | _ <- xs ]

myLength' xs = snd $ last $ zip xs [1..]

-- Problem 5
-- Reverse a list.

myReverse :: [a] -> [a]
myReverse [] = []
myReverse (x:xs) = myReverse xs ++ [x]

myReverse' = foldl (flip (:)) []

-- Problem 6
-- Find out whether a list is a palindrome.
-- A palindrome can be read forward or backward; e.g. (x a m a x).
isPalindrome :: Eq a => [a] -> Bool
isPalindrome xs = xs == reverse xs

-- Problem 7
-- Flatten a nested list structure.
data NestedList a = Elem a | List [NestedList a]

flatten :: NestedList a -> [a]
flatten (Elem x) = [x]
flatten (List x) = concatMap flatten x


-- Transform a list, possibly holding lists as elements into a `flat'
-- list by replacing each list with its elements (recursively).

-- Problem 8
-- Eliminate consecutive duplicates of list elements.
-- If a list contains repeated elements they should be replaced
-- with a single copy of the element. The order of the elements
-- should not be changed.
compress :: Eq a => [a] -> [a]
compress []     = []
compress (x:xs) = [x] ++ (compress $ dropWhile (== x) xs)

-- Problem 9
-- Pack consecutive duplicates of list elements into sublists.
-- If a list contains repeated elements they should be placed
-- in separate sublists.
pack :: Eq a => [a] -> [[a]]
pack []     = []
pack (x:xs) = (x : takeWhile (==x) xs) : pack (dropWhile (==x) xs)

-- Problem 10
-- (*) Run-length encoding of a list. Use the result of problem P09
-- to implement the so-called run-length encoding data compression method.
-- Consecutive duplicates of elements are encoded as lists (N E) where N is
-- the number of duplicates of the element E.
encode :: Eq a => [a] -> [(Int, a)]
encode xs = map (\x -> (length x, head x)) (pack xs)
