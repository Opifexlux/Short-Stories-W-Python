#!/usr/bin/python3
#Author: Alvaro Islas


# Just the simple setup of the horoscope daytime.
import datetime
dt = datetime.datetime.now()
m = dt.month # get current month value
d = dt.day # get current day value

horo = "" # a string value to store horoscope
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

#Printing the month day and the horoscope of the day.
print("Month", m , "day", d)
print("Horoscope of the day:", horo)