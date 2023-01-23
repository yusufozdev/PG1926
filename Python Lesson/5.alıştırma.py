class School():
    okulTuru= "okul tipi"

    def __init__(self, okulAdı, okulTuru, ogretmen, ogrenci, sınıf):
        self.okulAdı = okulAdı
        self.okulTuru = okulTuru
        self.ogretmen = ogretmen
        self.ogrenci = ogrenci
        self.sınıf = sınıf

O1 = School("Gazi Şahin", "İlkÖğretim Okulu", 16, 300, 20)
O2 = School("Keçiören", "Anadolu Lisesi", 22, 452, 37)
O3 = School("Hacettepe", "Üniversitesi", 32, 1200, 54)

Schools = [O1, O2, O3]

for okul in Schools:
    print(okul.okulAdı, okul.okulTuru, okul.ogretmen, okul.ogrenci, okul.sınıf)