import sys
from time import time

    
def strt_factorial_rec(m):
    return main_factorial_rec(m)



def main_factorial_rec(m):      #ф-я знах факторіала через рекурсію
    if m == 0:
        return 1
    sys.setrecursionlimit(sys.getrecursionlimit() + 1)      #встановлюєм ліміт на глибину рекурсії так щоб ліміт був 'плаваючий'
    return main_factorial_rec(m - 1) * m


while True:
    try:
        n = int(input("Введіть число: "))
        break
    except ValueError:
        print("Тільки числа")


def factorial_cycle(m):#функція знаходження факторіалу ітерацією
    fctrial = 1
    while m > 1:
        fctrial *= m
        m -= 1
    return fctrial




start_time = time()             # час початку 
print(strt_factorial_rec(n))
finish_time =time()            # час зупинки 

print(f"Час виконання функції: {finish_time - start_time}")  # різниця часу 
print()



print("функція знаходження факторіалу циклом: ")
start_time = time()              # час початку 
print(factorial_cycle(n))

finish_time =time()             # час зупинки 
print(f"Час виконання функції: {finish_time - start_time}")      # різниця часу 

# Метод ітерації при обробці даних забирає меньше  пам'яті але рекурсія працює швидше .
