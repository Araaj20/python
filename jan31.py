#creating a set
my_set={1,2,3,4,5,6}
print(my_set)
#adding elements to aset
my_set.add(6)
print(my_set)
#Removing an element from a set
my_set.remove(3)
print(my_set)
#set opertation
set1={1,2,3,4,5}
set2={4,5,6,7,8}
union_set=set1.union(set2)
print(union_set)
intersection_set=set1.intersection(set2)
print(intersection_set)
difference_set=set1.difference(set2)
print(difference_set)
print(3 in set1)
print(9 is set1)
# in pyrhon set are unorder collection they dont suppurt indexing and slicing like sequence such as in list or string therefore isnt direct metod revserse set however if u want reverse the element of a set u can convert set to a list resvers the list and then back convert into set
original_set={1,2,3,4,5,}
print("original_set:",original_set)
#convert set to list,revserse the list and convert it back to set
reversed_set=set(reversed(list(original_set)))
print("Reversed set:",reversed_set)