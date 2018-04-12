/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

https://projecteuler.net/problem=3

*/

package main

import(
	"fmt"
	"math"
	"sort"
)


func is_prime(number int) bool {
	if number < 4 {
		return true
	}
	for x := 2; x < number/2+1; x++ {
		if number%x == 0 {
			return false
		}
	}
	return true
}

// first solution was too long, need to narrow the scope of the problem.
// iterate up from the bottom to the square root, check the reciprocial.
// initially I went top down from 1/3, which took too long!

func max_prime_factor(number int) int {
	// set the limit at the sqrt
	ceiling := math.Sqrt(float64(number))
	// create an array to store all the primes
	prime_factors := []int{}
	// stepping by 1, b/c the reciprocial may be a prime even if this is even!
	for i := 3; i < int(ceiling); i++ {
		if number % i == 0 {
			// is the low factor prime?
			if is_prime(i) {
				prime_factors = append(prime_factors, i)
			}
			// is the high factor prime?
			other_factor := number / i
			if is_prime(other_factor) == true {
				prime_factors = append(prime_factors, other_factor)
			}
		}
	}
	// sort the found factors, return the top one
	sort.Ints(prime_factors)
	return prime_factors[len(prime_factors)-1]
}


func main(){

	fmt.Println(max_prime_factor(600851475143))

}



