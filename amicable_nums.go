/*

Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, 
then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, 
the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284.

The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

https://projecteuler.net/problem=21

*/

package main

import (
	"fmt"
	"math"
)



func divisors(number int) []int {
	ceiling := math.Sqrt(float64(number))

	factors := []int{1}

	for i := 2 ; i < int(ceiling) ; i++{
		if number % i == 0 {
			factors = append(factors, i)
			factors = append(factors, number / i)
		}
	}
	return factors
}


func sum_divisors( factor_slice []int) int {
	total := 0
	for _, num := range factor_slice {
		total += num
	}
	return total
}


func amicable_check( number int) (bool, int, int) {

	div_num := divisors(number)

	total_div_num := sum_divisors(div_num)

	fmt.Println(number)
	fmt.Println(div_num)
	fmt.Println(total_div_num)
	fmt.Println("\n\n\n")


	div_num2 := divisors(total_div_num)

	total_div_num2 := sum_divisors(div_num2)

	if total_div_num2 == number && number != total_div_num {
		
		return true, number, total_div_num
	}

	return false, 0, 0
}

// get all the divisors of a number: x
// sum these together: y

// take all take all the divisors of y
// sum these together: z 

// does z == x?

func main(){

	all_amicable := []int{}
	total_amicable := 0
	for i := 2 ; i < 10000 ; i++{
		am_check, n1, n2 := amicable_check(i)
		if am_check == true {
			all_amicable = append(all_amicable, n1)
			all_amicable = append(all_amicable, n2)
			
			total_amicable += n1
			total_amicable += n2

			i = n2 // this is to skip beyond the pair so numbers don't repeat
		}
	}
	
	fmt.Println(all_amicable)
	fmt.Println(total_amicable)


}







