# 10. Program, który pobiera od użytkownika 5 liczb całkowitych i uporządkowuje je od najmniejszej do największej

a = input("Podaj liczbę a: ")
b = input("Podaj liczbę b: ")
c = input("Podaj liczbę c: ")
d = input("Podaj liczbę d: ")
e = input("Podaj liczbę e: ")

numbers = [int(a), int(b), int(c), int(d), int(e)]

def bubble_sort(list):
  control_check = 0
  list_length = len(list)

  while control_check < list_length - 1:
    control_check = 0
    for i in range(0, list_length - 1):
      if list[i] > list[i + 1]:
        temp = list[i]
        list[i] = list[i + 1]
        list[i + 1] = temp
      else:
        control_check += 1
  
  return list

print(bubble_sort(numbers))

# Poniżej wcześniejsze próby rozwiązania zadania, które finalnie doprowadziły mnie do właściwego rozwiązania.
# Przy okazji dowiedziałem się o istnieniu algorytmu sortowania bąbelkowego. Czuję satysfakcję z tego, że logikę takiego algorytmu wymyśliłem sam w trakcie pisania kodu,
# chociaż wiem że ten algorytm jest bardzo podstawowy i najbardziej intuicyjny przy rozwiązywaniu problemu sortowania liczb

# a = input("Podaj liczbę a: ")
# b = input("Podaj liczbę b: ")
# c = input("Podaj liczbę c: ")
# d = input("Podaj liczbę d: ")
# e = input("Podaj liczbę e: ")

# numbers = [a, b, c, d, e]
# #          5, 3, 7, 1, 9 
# min_max_order = [1, 1, 1, 1, 1]
# i = 0

# while i < 5:
#   for j in numbers:
#     if numbers[i] >= j:
#       min_max_order[i] = j
#       numbers.pop(i)
#   i += 1

# print(min_max_order)

# NOT FINISHED

# numbers = [a, b, c, d, e]

# 10. Program, który znajduje najmniejszą liczbę w tablicy

# def min_max_order_in_array(array):
#   array_length = len(array)
#   counter = 0

#   while counter < array_length:
#     state = array[counter]
#     for element in array:
#       if element < :
#         array.append(element)
#     array.remove(state)             # [9, 3, 8]
#     array.insert(counter, state)    # [1, 9, 3, 8]
#     print(f"{counter}. {array}")
    
#     counter += 1
  
#   return array

# print(min_max_order_in_array([9, 1, 3, 8]))

# NOT FINISHED

# def min_max_order_in_array(array):
#   control_check = 0
#   array_length = len(array)
#   while control_check < array_length:
#     control_check = 0
#     for element in array:
#       state = None
#       if array.index(element) + 1 >= array_length:
#         continue
#       elif element > array[array.index(element) + 1]:
#         print(f"element: {element}, element + 1: {array[array.index(element) + 1]}") # //
#         state = array[array.index(element) + 1]
#         array.pop(array.index(element) + 1)
#         array.insert(array.index(element), state)
#         print(array)
#       else:
#         control_check += 1

#   return array

# print(min_max_order_in_array([9, 1, 3, 8, 7, 32, 15, 2]))

# Powyższe chyba idzie w dobrym kierunku. Control check powinine działać tak: iteruje po tablicy i jest inkrementowany tylko w momencie,
# gdy w danej parze (wewnątrz for_in) nie dochodzi do zamiany kolejności, i tak do momentu aż całe przejście pętli for zwóróci tylko braki podmian,
# to będzie oznaczało że nie ma już żadnej pary której kolejności można podmienić, więc while powinien zostać zakończony;