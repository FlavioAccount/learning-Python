#Keyword arguments = an argument proceded by an identifier
#                   helps with readability
#                   order of arguments doesn't matter
#                   1. positional   2. default  3. KEYWORD  4. arbitrary
#------------------------------------------------------------------------------
#Define the inputs positions of each function
# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")

# hello(greeting="Hello", title="Mr", last="Spongebob", first="Squarepanths")

#------------------------------------------------------------------------------
def get_phone(country, area, first, last):
    return f"{country}--{area}--{first}--{last}"

phone_num = get_phone(country =1, area=123, first=456, last=7890)
print(phone_num)