variable = None
dizi = []
x = 0

while True:
    variable = input("Lütfen veri giriniz. :")

    try:
        if variable == "c":
            break
        else:
            dizi.append(int(variable))
    except:
        print('Lütfen sayı giriniz. :')


print(format(dizi))

for i in dizi :
    if i % 2==1 and i>=x :
        x=i

print('En büyük tek sayı : ', x)