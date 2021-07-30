#1. Дано целое число (int). Определить сколько нулей в этом числе.

num = 10000
print(num)
num_str = str(num)
result = num_str.count("0")
print(result)


# zero_count = 0
#
# while num > 0:
#     digit = num % 10
#     if digit == 0:
#         zero_count += 1
#     num = num / 10
#
# print(zero_count)

#2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
print("#####################################################")
print("Задание №2")

number = 507607000
print(number)
str_number = str(number)
number_revers = str_number[::-1]
number_revers = str(int(number_revers))
result = len(str_number) - len(number_revers)
print(result)


# count = 0
# while n % 10 == 0:
#     count += 1
#     n //= 10
# print(count)

#3. Даны списки my_list_1 и my_list_2.
#Создать список my_result в который вначале поместить
#элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
print("#####################################################")
print("Задание №3")

my_list_1 = [96,87,78,69]
my_list_2 = [69,420,69,420]
my_result = []

for index in range(len(my_list_1)):
    if index % 2 == 0:
        my_result.append(my_list_1[index])

for index, element in enumerate(my_list_2):
    if index % 2 != 0:
        my_result.append(element)

print(my_result)

#4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
#стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
print("#####################################################")
print("Задание №4")

my_list = [13,14,15,16]
print(my_list)

new_list = my_list[1:]
first_place = my_list[0]

# new_list.remove(first_place)

new_list.append(first_place)
print(new_list, my_list)

#5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
#[1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
print("#####################################################")
print("Задание №5")

my_list = [13,14,15,16]
print(my_list)


first_place = my_list.pop(0)
my_list.append(first_place)


print(new_list)

#6. Дана строка в которой есть числа (разделяются пробелами).
#Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
#Для данного примера ответ - 133. (используйте split и проверку isdigit)
print("#####################################################")
print("Задание №6")

txt = "69 меньше чем 420 но больше чем 21"

digits = []
words = txt.split()
for word in words:
    if word.isdigit():
        digits.append(int(word))
result = sum(digits)
print(result)

# def sum_digits_string(str1):
#     sum_digit = 0
#     for x in str1:
#         if x.isdigit() == True:
#             z = int(x)
#             sum_digit = sum_digit + z
#
#     return sum_digit
#
#
# print(sum_digits_string(txt))
# #Не работает почему-то

#7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
#которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
#В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
#my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
print("#####################################################")
print("Задание №7")

my_str = "My long string"
print(my_str)

l_limit = "o"
r_limit = "g"
l_limit_pos = my_str.find(l_limit)
r_limit_pos = my_str.rfind(r_limit)

sub_str = my_str[l_limit_pos + 1:r_limit_pos]
print(sub_str)


#8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
#Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
#быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
#(используйте срезы длинны 2)
print("#####################################################")
print("Задание №8")
my_str = "ashdgfjsdhfjhd"
for index in range(0, len(my_str), 2):
    print(my_str[index: index + 2])

#9. Дан список чисел. Определите, сколько в этом списке элементов,
#которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
#Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
#Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
print("#####################################################")
print("Задание №9")
# my_list[index] > my_list[index-1] + my_list[index+1]