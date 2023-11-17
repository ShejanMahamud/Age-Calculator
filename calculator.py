from datetime import datetime

# Get user's birthdate
birthdate = input("Enter your birthdate (YYYY-MM-DD): ")

# Calculate current date
current_date = datetime.now()

# Convert birthdate string to datetime object
birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

# Calculate the difference between current date and birthdate
age = current_date - birthdate

# Calculate years, months, and days
years = age.days // 365
remaining_days = age.days % 365
months, days = divmod(remaining_days, 30)

# Print the user's age
print(f"You are {years} years, {months} months, and {days} days old.")
