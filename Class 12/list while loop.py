lst = []
n = int(input("Enter number of elements in list: "))

for i in range(0, n):
   print("Enter element: ".format(i+1))
   elm = int(input())
   lst.append(elm) 
print("The entered list is: \n",lst)

start = 0
end = len(lst)


while start < end:
    if lst[start] > 120:
        break
    if lst[start]%10==0:
        print("Numbers divisble by 10 and less than 120 are: \n", lst[start])
    

    start+=1
