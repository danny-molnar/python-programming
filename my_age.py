import datetime
now = datetime.datetime.now()

year = input("Which year were you born? ")
age = now.year - int(year)
print(f"Your age is:  {str(age)}")