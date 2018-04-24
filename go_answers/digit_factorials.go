/*
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

https://projecteuler.net/problem=34

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

func DigitFactorials(number big.Int) big.Int {
	dig_total := big.NewInt(0)

	for _, dig := range number.String() {
		temp := int(dig - '0')
		fact_val := Factorial(temp)
		dig_total.Add(dig_total, &fact_val)
	}
	return *dig_total
}

func main() {

	sum_dig_factorials := 0

	for i := 10; i < 362880; i++ {
		number := big.NewInt(int64(i))
		sum_factorials := DigitFactorials(*number)

		if sum_factorials.Cmp(number) == 0 {
			fmt.Println(number.String())
			sum_dig_factorials += i
		}
	}

	fmt.Println(sum_dig_factorials)
}
