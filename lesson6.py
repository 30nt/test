#1. Дан список строк my_list. Создать новый список в который поместить
#элементы из my_list по следующему правилу:
#Если строка стоит на нечетном месте в my_list, то ее заменить на
#перевернутую строку. "qwe" на "ewq".
#Если на четном - оставить без изменения.
#Задание сделать с использованием enumerate или range.

def func(my_list):
    new_list = my_list.copy() # создаем массив, который будем изменять
    for index in range(len(my_list)): # проходим по всем элементам
        if index % 2: # если элемент четный
            new_list[index] = my_list[index][::-1] # переворачиваем строку
    return new_list


array = ["abc", "qwe"]

print(func(array), array)

#2. Дан список строк my_list. Создать новый список в который поместить
#элементы из my_list у которых первый символ - буква "a".
print("#####################################################")
print("Задание №2")

def func2(mylist):
    new_list = []
    for value in mylist:
        if value[0] == "a":
            new_list.append(value)
    return new_list

print(func2(["allo", "privet"]))

#3. Дан список строк my_list. Создать новый список в который поместить
#элементы из my_list в которых есть символ - буква "a" на любом месте.
print("#####################################################")
print("Задание №3")
#k = -1

def func2(mylist):
   new_list = []
   for value in mylist:
       if "a" in value:
           new_list.append(value)
   return new_list

print(func2(["allo", "privet"]))

#4. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
#Например [1, 2, 3, "11", "22", 33]
#Создать новый список в который поместить только строки из my_list.
print("#####################################################")
print("Задание №4")

def func(mylist):
    new_list = [] #новый список в который будем записывать строки из входного массива
    for i in mylist: # проходим по всему входному массиву
        if type(i) == str: # проверяем строка ли (для этого тип элемента сравниваем с типом строки)
            new_list.append(i) # добавляем в выходной массив строку

    return new_list

array = [1,2,"hello", "ghrh", 3]

print(func(array))
#5. Дана строка my_str. Создать список в который поместить те символы из my_str,
#которые встречаются в строке ТОЛЬКО ОДИН раз.
print("#####################################################")
print("Задание №5")

my_str = 'Привет как дела                                                           '
lst = []
[lst.append(i) for i in set(my_str) if my_str.count(i) == 1]
print(lst, list(set(my_str)))

#6. Даны две строки. Создать список в который поместить те символы,
#которые есть в обеих строках хотя бы раз.
print("#####################################################")
print("Задание №6")

str1_ = "Белая машина"
str2_ = "Красный мотоцикл"
# res = []
# new_str = str1_ + str2_
# for symbol in new_str:
#     if symbol not in res:
#         res.append(symbol)

res = list(set(str1_).union(set(str2_)))
print(res)


#7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
#но в каждой ТОЛЬКО ПО ОДНОМУ разу.
print("#####################################################")
print("Задание №7")

str1_ = "Белая машина"
str2_ = "Красный мотоцикл"
new_str = str1_ + str2_
res = []
for symbol in new_str:
    if str1_.count(symbol) == 1 and str2_.count(symbol) == 1 and symbol not in res:
        res.append(symbol)
print(res)