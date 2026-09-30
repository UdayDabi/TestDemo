
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4,'e': 5}

print(d)

print("Value for key 'b':", d.get('b'))  # Output: 2
print(d.keys())
print(d.values())
print("d.items():", d.items())
# d.clear()
print(d)
# d.pop('c')
# print("d after pop('c'):", d)
# d.popitem()
# print("d after popitem():", d)
d.update({'c': 6, 'a': 7})
print("d after update():", d)
d.setdefault('e', 8)
print("d after setdefault():", d)