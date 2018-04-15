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
	//"math/big"
	"strconv"
)


func Factorial(number int) int {
	output := number

	for i := (number -1); i > 0; i++ {
		output = output * i
	}
	return output
}

func DigitSum(number int) int{
	total := 0

	for _, i := range strconv.Itoa(number){
		temp := int(i - '0')
		total += temp
	}
	return total
}


func main(){
	z := 12345
	x := strconv.Itoa(z)
	fmt.Println(x)


	for _ , i := range x {
		temp := int(i - '0')
		//fmt.Printf("character %v\t number:%v\n", temp, strconv.ParseInt(temp) )
		fmt.Printf("%v\n", temp)
		fmt.Printf("%v\n", temp *2)
	}

 
	//fact_total := Factorial(100)

	digit_total := DigitSum(15)

	fmt.Println(digit_total)
}