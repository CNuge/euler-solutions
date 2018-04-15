/*

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,

and the sum of the digits in the number 10!
is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!


https://projecteuler.net/problem=20

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

func BigDigitSum(number big.Int) int {
	total := 0

	for _, i := range number.String() {
		temp := int(i - '0')
		total += temp
	}
	return total
}

func main() {

	fact_total := Factorial(100)
	fmt.Println(fact_total.String())

	fact_digit_total := BigDigitSum(fact_total)
	fmt.Println(fact_digit_total)

}
