list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["apple", "banana", "cherry"]
list2 = ["mango", "pineapple", "papaya"]
for x in list2:
    list1.append(x)
print(list1)

list1 = ["apple", "banana", "cherry"]
list2 = ["mango", "pineapple", "papaya"]
list1.extend(list2)
print(list1)
