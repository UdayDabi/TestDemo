
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4,'e': 5}

print(d)
print(d.get('c'))  # Output: 1
print(d.keys())
print(d.values())
print(d.items())
# d.clear()
# print(d)
d1=d.copy()
print(d1)
# d.popitem()
# print(d)
# d.pop('c')
# print(d)
print(d.__len__())
d.update({'e': 6, 'g': 8})
print(d)
d.setdefault('e', 10)
print(d)
