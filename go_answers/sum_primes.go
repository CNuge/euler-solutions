/*

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

https://projecteuler.net/problem=10

*/

package main

import (
	"fmt"
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

func sum_primes(below int) int {
	total := 2
	// need to start with 2 accounted for, increment from 3 upwards
	//increment by 2, no need to check even numbers
	for i := 3; i < below; i = i + 2 {
		if is_prime(i) == true {
			total += i
			fmt.Printf("count: %v, sum_prime:%v\n", i, total)
		}
	}
	return total
}

func main() {
	fmt.Println(sum_primes(2000000))
}
