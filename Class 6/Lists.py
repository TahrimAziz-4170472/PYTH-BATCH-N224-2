
# Declare - empty

lst = []

print(type(lst)) 

lst2 = list()
print(type(lst2))  

# Declare - value

lst3 = [1,2,[3,4]]
 
print(lst3)

# Access Element

print(lst3[1])

print(lst3[-2])

print(lst3[0:2])

print(lst3[2])

print(lst3[0:])

print(lst3[:2])

# Length

print(len(lst3))

# Adding

lst4 = [5,6,7,8,9]
lst4.append(10)
print(lst4)

lst5 = [1,3,5]
lst5.insert(0, "C++")
print(lst5)

lst6 = [2,4,6,8]
lst7 = [1,3,5]
lst6.extend(lst7)
print(lst7)

lst8 = [2,8,16]
lst8.reverse()
print(lst8)

# Value Update - Mutable

lst9 = ["Python", "Java", "C++"]
lst9[0] = "JavaScript"
print(lst9)

# Remove

lst10 = [10,20,30,40,50]
lst10.remove(10)

print(lst10)

lst11 = [1,2,3,4,5]
lst11.pop()
print(lst11)

lst12 = [6,7,8,9,0]
lst12.pop(2)
print(lst12)
