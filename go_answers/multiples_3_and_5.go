package main


import(
	"fmt"
)



func main(){
	total := 0
	max := 1000

	for i := 0 ; i < max ; i++ {
		if (i % 3 == 0) || (i % 5 == 0){
			total += i
		}
	}

	fmt.Println(total)

}