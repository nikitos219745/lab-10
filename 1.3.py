from random import randint
from time import time
import sys






def main(q):
    return max_index_recursion(q)

def max_index_recursion(q, g=0, t=0, first_position=0, second_position=0):  
    if t == len(q[g]):
        g += 1  # проходимся  по рядку
        t = 0         
    if g == len(q):
        return first_position, second_position
    if q[g][t] > q[first_position][second_position]:  # умова
        first_position = g                      # рядок макс елемента
        second_position = t                     # стовпчик макс елемента
    t += 1

    sys.setrecursionlimit(sys.getrecursionlimit() + 1)  # зміна глибини рекурсії
    return max_index_recursion(q, g, t, first_position, second_position)






def max_index_cycle(q):
    first_position = 0  # рядок макс елемента
    second_position = 0  # стовпчик макс елемента
    g = 0
    while g != len(q):
        t = 0
        while t != len(q[g]):  
            if q[g][t] >q[first_position][second_position]:  # умова
                first_position, second_position = g, t
            t += 1
        g += 1
    return first_position, second_position



qq = []  # генеруємо рандомний список елементів 1 <= n <=5

n = randint(10, 50)

for i in range(n):

    g = []

    for j in range(n):

        g.append(randint(1, 11))

    qq.append(g)

print("Рандомний масив n*n", qq)





print("функція для обчислення індексу максимального елемента масиву , де 1<=n<=5 рекурсією: ")
start_time = time()              # час початку 
print(main(qq))
finish_time =time()             # час зупинки 
print(f"Час виконання функції: {finish_time - start_time}")      # різниця часу 





print("функція для обчислення індексу максимального елемента масиву , де 1<=n<=5 циклом: ")

start_time = time()              # час початку 
print(max_index_cycle(qq))
finish_time =time()             # час зупинки 
print(f"Час виконання функції: {finish_time - start_time}")      # різниця часу 
