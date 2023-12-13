mylist = [22,13,14,87,6,65,98,74,51,53]
result = list(filter(lambda x : (x % 13 == 0 ),mylist))
print(result)