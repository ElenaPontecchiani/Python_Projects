list1 = [1,2,3,4,5,6]
list2 = ["one", "two", "three", "four", "five", "six"]
#se l delle liste sono diverse gli el di tropppo sono ignorati
zipped = list(zip(list1,list2))
print(zipped)

unzipped = list (zip(*zipped))
print(unzipped)


for (l1,l2) in zip(list1,list2):
    print(l1)
    print(l2)