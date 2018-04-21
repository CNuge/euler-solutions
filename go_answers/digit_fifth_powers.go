/*
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.

https://projecteuler.net/problem=30
*/

package main

import (
	"fmt"
	"math"
	"strconv"
)

func digit_powers(number int, power float64) bool {
	// take a number and calculate if the sum of its digits equal
	dig_string := strconv.Itoa(number)

	total := 0.0

	for _, dig := range dig_string {
		single_int, _ := strconv.Atoi(string(dig))
		val := math.Pow(float64(single_int), power)
		total += val
	}

	if int(total) == number {
		return true
	}

	return false
}

func find_power_digits(power float64) []int {
	numbers_matching := []int{}
	for i := 2; i < 10000000; i++ {
		if digit_powers(i, power) == true {
			numbers_matching = append(numbers_matching, i)
		}
	}
	return numbers_matching
}

func main() {

	power_digits := find_power_digits(5.0)

	fmt.Println(power_digits)
	total := 0

	for _, i := range power_digits {
		total += i
	}

	fmt.Println(total)
}

/*{
	x := 2019
	z := strconv.Itoa(x)
	fmt.Println(z)

	for _, i := range z {
		back := string(i)
		fmt.Println(back)
		back2, _ := strconv.Atoi(back)
		fmt.Println(back2)

		fmt.Println(back2*5)

	}
}

*/
