list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
iterate_var = iter(list1)
for i in iterate_var:
    if i%2==0:
        print(i)
list = ["apple","banana","kiwi","pine apple","grapes"]
a = [i for i in list if "a" in i]
print(a)