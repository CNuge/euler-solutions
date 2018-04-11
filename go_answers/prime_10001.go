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

func iterate_primes(max_prime int) (int, int) {
	prime_count := 0
	number := 1
	for prime_count < max_prime {
		number++
		if is_prime(number) == true {
			prime_count++
		}
	}
	return number, prime_count
}

func main() {

	fmt.Println(iterate_primes(10001))

}
