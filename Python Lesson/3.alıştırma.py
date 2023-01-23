list = []
sıfır = []
degısken = True

print("Lütfen listeye yazılıcak sayıları giriniz.\n"
			"Ekleme bitti ise 1 tuşuna basabilirsiniz.")

while degısken:
		number = input()
		if number == 1:
				break
		else:
			list.append((int)(number))

print("Listenin Başlangıcı : \t", list)

for sıfır in list:
		if zeros == 0:
				sıfır.append(sıfır)
				myList.remove(sıfır)

list = sıfır + list
print("Son Hali : \t", list)
