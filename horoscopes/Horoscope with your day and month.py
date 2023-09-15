#!/usr/bin/python3
#Author: Alvaro Islas

#This is a horoscope without the account for leapyear. 


# take user input and save them into variables. 
m = int(input("Enter the month: "))
d = int(input("Enter the day: "))


# validate input and make sure the user isn't inputting invalid data. 
if (m <1 or m > 12):
	print("Month value must be 1 ~ 12")
elif (d < 1 or d > 31):
	print("Day value must be 1 ~ 31")

else:
    # match the horoscope
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
# Print your answer. 
    print("Your horoscope:", horo)