tuple_1 = ()

print(type(tuple_1)) 

print(tuple_1)
tuple_2 = tuple()
print(type(tuple_2))

tuple_1 = ("Python", 10, 10.5, [10, 20, 30], (10, 20, 30,40))
print(tuple_1)  



print(tuple_1[0])  
print(tuple_1[-1])  

print(tuple_1[0:3])  


tuple_3 = (10, 20)
tuple_3 = tuple_1 + tuple([10, 30])
print(tuple_3)

lst = [10.5, 20]
print(lst)
tpl = tuple(lst)
print(tpl)

lst_2 = list(tpl)
print(lst_2)

lst_2.append(20)

tpl_2 = tuple(lst_2)
print(tpl_2)
