/*
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

curl https://projecteuler.net/project/resources/p022_names.txt > names.txt

https://projecteuler.net/problem=22

*/

package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"sort"
	"strings"
)

// determine name score
// map to get the value a = 1, b = 2
func NameScore(name string) int {
	var letter_map = map[rune]int{
		'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
		'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
		'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

	total := 0
	for _, i := range name {
		total += letter_map[i]
	}

	return total
}

// multiply by the position in the sorted list.
func NameScoresTotal(name_list []string) int {
	total := 0

	for i, name := range name_list {
		n_score := NameScore(name)
		n_total := (i + 1) * n_score
		total += n_total
	}
	return total
}

func main() {
	// read in the data
	file, err := ioutil.ReadFile("names.txt")
	if err != nil {
		log.Fatal(err)
	}

	//split names on delimiter
	name_data := strings.Split(string(file), ",")
	// sort name list
	sort.Strings(name_data)

	output := NameScoresTotal(name_data)
	fmt.Println(output)

}
