l = [1, 2, 3, 4, 5]

list_it = iter(l) # у list есть встроенный итератор, вот так то

print(list_it)

try:
    while True:
        print(next(list_it), end=' ')
except StopIteration:
    pass

