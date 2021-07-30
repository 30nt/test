# 1

value = 102

if value < 100:
    new_value = value/2
else:
    new_value = - value

new_value = value/2 if value < 100 else - value
print(new_value)

if value < 100:
    new_value = True
else:
    new_value = False
print(f"new_value = {new_value}")


my_list = [7,11,13,17, 12,34,456,67]

if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])

print(my_list[::-1])

value = float(input('Input a decimal nunber'))
print(value)
answer = value ** -1
print(answer)