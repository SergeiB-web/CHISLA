str1 = "HELLO_WORLD"
print("Весь список:",str1[0:11:1])
print("Нечётные по порядку элементы:",str1[0:11:2]) #start:stop:step
print("Чётные по порядку элементы:",str1[1:11:2])
print("Все элементы в обратном порядке:",str1[-1:-12:-1])
print("Все элементы, начиная с шестого:",str1[5:11:1])
print("Все элементы, не доходя до шестого:",str1[0:5:1])
print("Все элементы от предпоследнего до третьего в обратном порядке:",str1[9:-9:-1])