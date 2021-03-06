/*
Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5

If they are then placed in numerical order, with any repeats removed,
 we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

https://projecteuler.net/problem=29
*/

package main

import (
	"fmt"
	"math/big"
)

func AppendIfUnique(subject []big.Int, query big.Int) []big.Int {
	for _, i := range subject {

		if i.Cmp(&query) == 0 {
			return subject
		}
	}
	subject = append(subject, query)
	return subject
}

func PowerListHundred() []big.Int {
	outlist := []big.Int{}
	for i := 2; i <= 100; i++ {
		for j := 2; j <= 100; j++ {
			v1 := big.NewInt(int64(i))
			v2 := big.NewInt(int64(j))
			val := big.NewInt(int64(0))

			val.Exp(v1, v2, nil)
			outlist = AppendIfUnique(outlist, *val)
		}
	}
	return outlist
}

func main() {
	uniqe_powers := PowerListHundred()

	fmt.Println(len(uniqe_powers))

}
