#!/usr/bin/python3
#Author: Alvaro Islas

#inputing your birth year, your month, and day to find your Zodiac. 

# check leap year date to adjust. 
def CheckLeapYear(y):
	max=0
	if (y % 4) == 0:
		if (y % 100) == 0:
			if (y % 400) == 0:
				max = 29
			else:
				max = 28
		else:
			max = 29
	else:
		max = 28
	return max

# take the user input and store them into variables. 
y = int(input("Enter your birth year: "))
m = int(input("Enter the month: "))
d = int(input("Enter the day: "))

# validate input in order that we don't have users putting in some random date. 
if (m <1 or m > 12):
	print("Month value must be 1 ~ 12")
elif (d < 1 or d > 31):
	print("Day value must be 1 ~ 31")
elif ( (m == 4 or m==6 or m==9 or m==11) and d > 30):
	print("Maximum day of month is 30.")
elif ( m == 2 and d > CheckLeapYear(y)):
	print("Maximum is 28 for regular year or 29 for leap year.")
else:
    # match the horoscope with the data given from the user. 
    if (m == 1 and d >= 20) or (m == 2 and d < 12):
        horo = "Aquarius"
    elif (m == 2 and d >= 12) or (m == 3 and d < 21):
        horo = "Pisces"
    elif (m == 3 and d >= 21) or (m == 4 and d < 20):
        horo = "Aries"
    elif (m == 4 and d >= 20) or (m == 5 and d < 21):
        horo = "Taurus"
    elif (m == 5 and d >= 21) or (m == 6 and d < 21):
        horo = "Gemini"
    elif (m == 6 and d >= 21) or (m == 7 and d < 23):
        horo = "Cancer"
    elif (m == 7 and d >= 23) or (m == 8 and d < 23):
        horo = "Leo"
    elif (m == 8 and d >= 23) or (m == 9 and d < 23):
        horo = "Virgo"
    elif (m == 9 and d >= 23) or (m == 10 and d < 23):
        horo = "Libra"
    elif (m == 10 and d >= 23) or (m == 11 and d < 22):
        horo = "Scorpio"
    else:
        horo = "Sagittarius"
# Your horoscope print.
    print("Your horoscope:", horo)