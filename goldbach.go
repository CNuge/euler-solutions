/*
It was proposed by Christian Goldbach that every odd composite number can 
be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime 
and twice a square?


https://projecteuler.net/problem=46

*/

package main

import(
	"fmt"
	"math"
)

func IsPrime(number int) bool {
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


func SquareCheck(number int) bool {
	int_root := int(math.Sqrt(float64(number)))
	return (int_root * int_root) == number
}

func PrimeAndTwiceSquare(number int) bool {
	for i := number - 1 ; i > 0; i--{
		if IsPrime(i) == true {
			rem := number - i
			half_rem := float64(rem)/2

			if float64(int(half_rem)) == half_rem {
				if SquareCheck(int(half_rem)) == true{
					return true
				}			
			}
		}
	}

	return false

}

func FindGoldbach() int{
	for i := 3; ; i = i + 2{
		if IsPrime(i) != true{
			if PrimeAndTwiceSquare(i) == false {
				return i
			}
		}
	}
}

func main(){
	rem := 7
	fmt.Println(rem/2)
	fmt.Println(SquareCheck(25))
	fmt.Println(FindGoldbach())
}