def gen_f():
    yield 1
    yield 2


gen_obj = gen_f()

for el in gen_obj:
    print(type(el), el, end=' ')
print()

print(gen_obj)  # gen_obj по которому мы ходим и итератор от gen_obj = это одно и то же

iterator = iter(gen_obj)
print(iterator)