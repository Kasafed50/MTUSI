li = []

while True:
    try:
        getCount = int(input('Введите кол-во чисел, которые хотите ввести: '))
        if getCount < 3:
            raise Exception()
        break
    except Exception as e:
        print('Неверное значение, повторите попытку')

getCount += 1

for z in range(1, getCount):
    while True:
        try:
            li_add = int(input("Введите число: "))
            if li_add < 1:
                raise Exception()
            li.append(li_add)
            break
        except Exception as e:
            print('Неверное значение, повторите попытку')

a = 0
b = 0
c = 0

for i in range(len(li) - 3):
    a = li[i]
    b = li[i + 1]
    c = li[i + 2]
    if a < b + c and b < a + c and c < b + a:
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        break

print(s, a, b, c)