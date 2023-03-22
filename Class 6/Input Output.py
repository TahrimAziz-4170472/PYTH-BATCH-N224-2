# Display Process - 01

print("Hello Tahrim", end=" ")
print("Aziz")

# Display Process - 02

language = "Python"

print("Hello ", language, " and Java")

# P - 03

country = "France"
country2 = "England"

print('Country one is: {} and Country two is: {}'.format(country, country2))
print("Country one is: {c2} and Country two is: {c1}".format(c1=country, c2=country2))

# P - 04

print(f"Countries are {country} and {country2}")
print(f'Countries are {country2} and {country}')

# P - 05

num = 10.19181843847575

"""
%f - float
%d - int 
%s - string
"""

print(num)

print("%.3f" % num)

print("%d" % num)

print("%s" % country)

print("Countries are %s and %s" % (country, country2))
