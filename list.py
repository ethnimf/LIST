my_list = [22, 34, 45, 45, 28, 93, 95]
my_list1 = [11, 23, 45, 51, 94, 98 ,30]

sum_of_list = sum(my_list)
print("Сумма элементов списка:", sum_of_list)

max_number = max(my_list)
print("Поиск наибольшего элемента:", max_number)

ints_my_list = list(set(my_list)) 
print("Удаление дубликатов:", ints_my_list)

res = [*my_list, *my_list1] 
print ("Объединение списков:", str(res))

colours = ("blue", "pink", "black", "yellow")
index = colours.index("black")
print ("Поиск элемента в кортеже:", index)

tuple1 = (1, 3, 4, 8, 9)
tuple2 = (5, 7, 3, 6, 7)
sum = tuple1+tuple2
print("Слияние кортежей:", sum)

my_tuple = ("тело", "рука", "голова", "нога")
my_list = list(my_tuple)
my_list.remove("рука")
print ("Удаление элемента из кортежа:", my_list)

marks = (2, 4, 4, 4, 5, 3, 5)
count = marks.count(4)
print ("Подсчет элементов в кортеже:", count)

