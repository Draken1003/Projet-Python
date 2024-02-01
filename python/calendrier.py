# Créé par hetit, le 05/10/2023 en Python 3.7
import calendar

year = 2023
month = 1
for i in range(12):
    print(calendar.month(year, month))
    month += 1


