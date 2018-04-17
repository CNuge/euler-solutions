/*
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

https://projecteuler.net/problem=25
*/

package main

import (
	"fmt"
	"math/big"
)

func ThouDigFib() (int, string) {

	a := big.NewInt(1)
	b := big.NewInt(1)
	temp := big.NewInt(0)

	for i := 2; ; {
		temp = big.NewInt(0)
		temp.Add(b, a)

		a = b
		b = temp
		i++

		if len(b.String()) >= 1000 {
			return i, b.String()
		}
	}

}

func main() {

	x, y := ThouDigFib()
	fmt.Println(x)
	fmt.Println("\n\n")
	fmt.Println(y)

}
