t = {1,2,3}
t[0] = 10

'''
fruits = ['Juice', 'Tomato', 'Potatoes', 'Banana', 'Tomato', 'Banana']

results = []
for item in fruits:
    count = 1
    while fruits.count(item) > 1:
        count += 1
        fruits.remove(item)
    results.append((item, count))

print(results)
'''

'''def filterDup(list):
    for item in list:
        while list.count(item) > 1:
            list.remove(item)         #also use: del list[list.index(item)]
    return list

print(filterDup(["tom", "jerry", "dog", "tom"]))'''
