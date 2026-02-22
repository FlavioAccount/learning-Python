# Match-case statement (switch): An alternative to using many ´elif´ statements
#                               Execute some code if a value matches a 'case'
#                               Benefits: cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _: #This is a wild card. If nothing matches the cases above, it will perform the step bellow
            return "Not a valid day"

# day = int(input("Type the day of the week: "))
# print(day_of_week(day))

#------------------------------------------------------------------------------------------------------------------
#This function checks if it is a weekend day

def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return "It is weekend"
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "It is a week day"
        case _: #This is a wild card. If nothing matches the cases above, it will perform the step bellow
            return "Not a valid day"
day = int(input("Type a week day: "))
#print(type(day_of_week(day)))
print(is_weekend(day_of_week(day)))
