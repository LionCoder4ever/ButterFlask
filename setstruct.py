some_list = ['a','b','n','g','n','a','n']

#get the repeat value

duplicates = []
for value in some_list:
    if some_list.count(value)>1:
        if value  not in duplicates:
            duplicates.append(value)

print(duplicates)


duplicates = set([x for x in some_list if some_list.count(x)>1])
print(duplicates)