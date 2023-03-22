key1 : "Python"
key2 : "Python"

my_dict = {}
print(type(my_dict))  

my_dict2 = dict()
print(type(my_dict2)) 



my_dict = {
    "name": "Tahrim Aziz",
    "language": "Bangla",
    "one": 1,
    "decimal": 1.5,
    "lst": [1, 2, 3, 4],
    1: "One"
}
print(my_dict)  

my_dict2 = dict(
    {
    "name": "Tahrim Aziz",
    "language": "Bangla",
    "one": 1,
    "two": 2,
    "decimal": 1.5,
    "lst": [1, 2, 3, 4]
    }
)
print(my_dict2)


print(my_dict["name"])  
print(my_dict.get("language"))  
print(my_dict["lst"])
print(my_dict[1])

my_dict3 = {
    1: 1,
    2: 2.5
}

print(my_dict3.get(2))


print("-----------------")
print(my_dict3)
my_dict3[1] = "One"

print(my_dict3)

my_dict3[3] = "Three"
print(my_dict3)


print(my_dict3.pop(1))
print(my_dict3)

my_dict3.clear()
print(my_dict3)
