#1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
print("#####################################################")
print("Задание №1")

my_list = [{"name": "John", "age": 15}, {"name": "Jack", "age": 45}, {"name": "Janett", "age": 25}]
# for value in my_list:
#     age = value["age"]
#     name = value["name"]

#а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
list_person = []
list_name = []
# max_age = 200
min_len = 0
sum_start = 0
for person in my_list:
    list_person.append(person["age"])
    list_name.append(len(person["name"]))

min_age = min(list_person)
max_name = max(list_name)
# for element in list_person:
#     if element < max_age:
#         max_age = element
for person in my_list:
    if person["age"] == min_age:
        print(person["name"])
#б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.

for person in my_list:
    if len(person["name"]) == max_name:
        print(person["name"])

#в) Посчитать среднее количество лет всех людей из списка.

average_age = sum(list_person) / len(list_person)
print(average_age)

#2) Даны два словаря my_dict_1 и my_dict_2.
print("#####################################################")
print("Задание №2")

my_dict_1 = {"name": "Ray",
             "age": 45,
             "les": "Ry"}
my_dict_2 = {"name": "Nick",
             "job": "actor"}
#а) Создать список из ключей, которые есть в обоих словарях.


my_dict_1_set_keys = set(my_dict_1.keys())
my_dict_2_set_keys = set(my_dict_2.keys())

res_a = list(my_dict_1_set_keys.union(my_dict_2_set_keys))
print(res_a)
#new_dict = {}
#for i in my_dict_1:
#    new_dict[i] = my_dict_2[i]
#print(new_dict)

#б) Создать список из ключей, которые есть в первом, но нет во втором словаре.

# res = dict((key, my_dict_1[key]) for key in my_dict_1 if key not in my_dict_2)
res_b = list(my_dict_1_set_keys.difference(my_dict_2_set_keys))
print(res_b)

#в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.

res = dict((key, my_dict_1[key]) for key in my_dict_1 if key not in my_dict_2)
print(res)

#г) Объединить эти два словаря в новый словарь по правилу:
#если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
#если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

#{1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

new_dict = my_dict_1.copy()
for key in my_dict_2:
    if key in new_dict:
        new_dict[key] = [my_dict_1[key], my_dict_2[key]]
    else:
        new_dict[key] = my_dict_2[key]
print(new_dict)