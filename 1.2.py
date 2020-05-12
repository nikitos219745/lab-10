from time import time

def main(n):  # допоміжна функція для обрахування пам'яті
    return cortex_recursion(n)



def summma_recursion(n):  
    if n < 10:
        return n
    return n % 10 + summma_recursion(n // 10)
    return



def cortex_recursion(n):  #  знаходим  цифровий корень рекурсією
    if n < 10:
        return n
    return cortex_recursion(summa_recursion(n))



def cortex_cycle(n):  #знаходим  цифровий корень  циклом
    s = str(n)
    while len(s) > 1:
        n = 0
        for i in s:
            n += int(i)
        s = str(n)
    return s



print("Функція виконання цифрового кореня рекурсією: ")

while True:
    try:
        n = int(input("Введіть число: "))
        break
    except ValueError:
        print("Тільки числа")



start_time = time()             # час початку 
print(main(n))
finish_time =time()            # час зупинки 
print(f"Час виконання функції: {finish_time - start_time}")  # різниця часу 
print()




while True:
    try:
        n = int(input("Введіть число: "))
        break
    except ValueError:
        print("Тільки числа")



start_time = time()             # час початку 
print(cortex_cycle(n))
finish_time =time()            # час зупинки 
print(f"Час виконання функції: {finish_time - start_time}")  # різниця часу 
print()
