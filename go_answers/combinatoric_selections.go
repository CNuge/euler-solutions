/*
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	n!
r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of

nCr, for 1 ≤ n ≤ 100, are greater than one-million?


https://projecteuler.net/problem=53
*/

package main

import (
	"fmt"
	"math/big"
)

func Factorial(number int) big.Int {
	output := big.NewInt(0)

	output.MulRange(int64(1), int64(number))

	return *output
}

func Combinatorial(n int, c int) big.Int {
	// Factorial(n)  / Factorial(r) * Factorial(n-r)
	numerator := Factorial(n)

	denom_a := Factorial(c)
	denom_b := Factorial(n - c)

	denom := big.NewInt(0)
	denom.Mul(&denom_a, &denom_b)

	n_choose_c := big.NewInt(0)

	n_choose_c.Div(&numerator, denom)

	return *n_choose_c
}

func main() {

	above_one_million := 0

	for n := 1; n <= 100; n++ {
		for c := 1; c <= n; c++ {
			combinations := Combinatorial(n, c)
			if combinations.Cmp(big.NewInt(1000000)) == 1 {
				above_one_million += 1
			}
		}
	}
	fmt.Println(above_one_million)
}
