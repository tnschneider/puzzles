primes :: [Integer]
primes = sieve [2..]
	where
		sieve (p:xs) = p : sieve [x | x <- xs, x `mod` p > 0]

primes' :: [Integer]
primes' = 2:([3..] `minus` composites)
	where
		composites = union [multiples pr | pr <− primes']

multiples n = map (n*) [n..]
(x:xs) `minus` (y:ys) | x<y = x:(xs `minus` (y:ys))
	| x==y = xs `minus` ys
	| x>y = (x:xs) `minus` ys
union = foldr merge []
	where
		merge (x:xs) ys = x:merge' xs ys
		merge' (x:xs) (y:ys) 	| x<y = x : merge' xs (y:ys)
								| x==y = x : merge' xs ys
								| x>y = y : merge' (x:xs) ys