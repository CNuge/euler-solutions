package main

/*

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

https://projecteuler.net/problem=2
*/

import (
	"fmt"
)

func fibSumEven(max int) int {
	a := 1
	b := 1
	temp := 0

	even_total := 0

	for {
		temp = 0
		temp = b + a

		a = b
		b = temp

		if a%2 == 0 {
			even_total += a
		}

		if max < b {
			return even_total
		}
	}
}

func main() {

	sum_even := fibSumEven(4000000)
	fmt.Println(sum_even)

}
