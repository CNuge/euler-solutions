"""

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

"""



def count_sundays(date_time, finish_year):
	mon_dict = {1 : 31,
			2 : 28,
			3 : 31,
			4 : 30,
			5 : 31 ,
			6 : 30,
			7 : 31,
			8 : 31,
			9 : 30, 
			10 : 31,
			11 : 30,
			12 : 31, }

	total_sundays = 0
	while date_time['year'] < finish_year + 1:
		print(date_time)
		if date_time['day_of_week'] == 7 :
			if date_time['day'] == 1 :
				total_sundays += 1
			date_time['day_of_week'] = 1
		else:
			date_time['day_of_week'] += 1 
		print(total_sundays)

		if date_time['day'] == mon_dict[date_time['month']]:
			#leap year monstrosity logic
			if date_time['month'] == 2 and date_time['year'] % 4 == 0:
				if str(date_time['year'])[-2:] != "00" or (str(date_time['year'])[-2:] == "00" and date_time['year'] % 400 == 0):
					date_time['day'] += 1
				else:
					date_time['day'] = 1
					date_time['month'] += 1
			# end of year
			elif date_time['month'] == 12:
				date_time['day'] = 1
				date_time['month'] = 1
				date_time['year'] += 1

			else:
				date_time['day'] = 1
				date_time['month'] += 1

		#this is for leap year extra days!
		elif date_time['day'] > mon_dict[date_time['month']]:
			date_time['day'] = 1
			date_time['month'] += 1

		else:
			date_time['day'] += 1

	return total_sundays

# a custom date time type structure
#sunday == 7

date_time = { 'day_of_week' : 2 , 
				'day' : 1, 
				'month' : 1, 
				'year' : 1901}


count_sundays(date_time, 2000)


