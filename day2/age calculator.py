age = input("how many year old are you????")
age_int=int(age)
day = age_int*365
month = age_int*12
week= age_int*52
message=f"you have left {day} days and {month} month and {week} weeks . so be alive more"
# its better to put this message in a variable cause it make it more comfortable
print(message)