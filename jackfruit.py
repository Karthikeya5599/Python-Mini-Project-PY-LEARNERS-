import datetime

print("AGE CALCULATOR")

#date of birth
day = int(input("Enter your birth day (1-31): "))
month = int(input("Enter your birth month (1-12): "))
year = int(input("Enter your birth year (e.g. 2005): "))

dob = datetime.date(year, month, day)

# today’s date
today = datetime.date.today()

age = today.year - dob.year

# if birthday has not come yet this year
if (today.month, today.day) < (dob.month, dob.day):
    age = age - 1

print("Your age is:", age, "years")
