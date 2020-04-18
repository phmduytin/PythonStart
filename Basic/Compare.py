name = 'abc'
# name2 = 'a' + 'b' + 'c'
# name2 = ''.join(['a', 'b', 'c'])
name2 = 'ABC'.lower()
if name == name2:
    print('Both of Equal')
else:
    print('Not equal')

if name is name2:
    print('Indentical')
else:
    print('Not Indentical')

print(id(name), id(name2))

if name is not name2:
    print('name is not name2')
