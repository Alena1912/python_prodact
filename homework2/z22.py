#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, 
#которые встречаются в обоих наборах. Пользователь вводит 2 числа.
#n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите число n: "))
m = int(input("Введите число m: "))

set1 = set()
set2 = set()
set3 = set()

print(f'Введите первое множество с {n} элементами: ')
for i in range(n):
    set1.add(int(input(f'n[{i}] = ')))
    
    
print(f'Введите второе множество с {m} элементами: ')
for i in range(m):
    set2.add(int(input(f'm[{i}] = '))) 
    

set3 = set.intersection(set1, set2)
          
b = list(set3)
b.sort()

for i in b:
    print(i, end = " ")

   