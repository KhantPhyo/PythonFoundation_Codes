from datetime import date
f_date = date.today()
print("Current Date : " ,f_date)
userinput_Date = int(input("Please enteryour input(Date) : "))
userinput_Month = int(input("Please enteryour input(Month-Number only) : "))
userinput_Year = int(input("Please enteryour input(Year) : "))
l_date = date(userinput_Year, userinput_Month, userinput_Date)
delta = l_date - f_date
print(delta.days)
