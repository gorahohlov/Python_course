# -------------

c = input('Введите целое положительное число: ')
l, i, d, c = len(c), 0, 0, int(c)
while i < l:
    d = max(c % 10, d)
    i += 1
#   c = c // 10
    c //=  10
#   print('iteration:', i)
print('Наибольшая цифра во введенном чилсе: ', d)
# -------------
