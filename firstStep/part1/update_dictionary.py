# не добавляйте кода вне функции
def update_dictionary(dict, key, value):
    if key in dict:
        dict[key] += [value]
        return
    key = key*2
    if key not in dict:
        dict[key] = [value]
    else:
        dict[key] += [value]

    # put your python code here

# Если ключ keykey есть в словаре dd, то добавьте значение valuevalue в список, 
# который хранится по этому ключу.

# Если ключа keykey нет в словаре, то нужно добавить значение в список по ключу 2 * key

# Если и ключа 2 * key нет, то нужно добавить ключ 2 * key в словарь 
# и сопоставить ему список из переданного элемента [value][value].
# не добавляйте кода вне функции
d = {}
(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)  