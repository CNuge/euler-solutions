/*
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a
century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?

https://projecteuler.net/problem=19
*/

package main

import (
	"fmt"
)

type DateTime struct {
	day_of_week int
	day         int
	month       int
	year        int
}

func (dt DateTime) String() string {
	return fmt.Sprintf("%v\t%v\t%v", dt.day, dt.month, dt.year)
}

func count_sundays(dt DateTime, finish_year int) int {
	var month_map = map[int]int{
		1:  31,
		2:  28,
		3:  31,
		4:  30,
		5:  31,
		6:  30,
		7:  31,
		8:  31,
		9:  30,
		10: 31,
		11: 30,
		12: 31}

	total_sundays := 0

	for dt.year < finish_year+1 {
		fmt.Println(dt)
		// check if the day is a sunday
		if dt.day_of_week == 7 {
			// check if its the first of the month
			if dt.day == 1 {
				total_sundays += 1
			}
			// reset day of week
			dt.day_of_week = 1
		} else {
			//incrementing day of wee
			dt.day_of_week += 1
		}
		// check if we need to roll over the month or the year, act accordingly
		if dt.day == month_map[dt.month] {
			// leap year fringe case
			if (dt.month == 2) && (dt.year%4 == 0) {
				// make sure its not a year divisible by 400
				yr_str := fmt.Sprintf("%v", dt.year)
				fmt.Println(yr_str[len(yr_str)-2:])
				if (yr_str[(len(yr_str)-2):] != "00") || ((yr_str[(len(yr_str)-2):] == "00") && (dt.year%400 == 0)) {
					dt.day += 1
				} else {
					dt.day = 1
					dt.month += 1
				}
			} else if dt.month == 12 {
				dt.day = 1
				dt.month = 1
				dt.year += 1
			} else {
				dt.day = 1
				dt.month += 1
			}
		} else if dt.day > month_map[dt.month] {
			dt.day = 1
			dt.month += 1
		} else {
			dt.day += 1
		}
	}
	return total_sundays
}

func main() {

	start_date := DateTime{
		day_of_week: 2,
		day:         1,
		month:       1,
		year:        1901,
	}

	fmt.Println(count_sundays(start_date, 2000))

}
