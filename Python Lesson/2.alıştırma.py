webKullanim = "qwertyuopasdfghjklizxcvbnm0123456789"
kAdiKullanim = "qwertyuopasdfghjklizxcvbnm0123456789-_"
noktaSonuKullanim = "qwertyuopasdfghjklizxcvbnm."


def mailDogrula(mailAdres, uzunluk):
    try:
        at = mailAdres.find("@")
        atCount = mailAdres.count("@")
        nokta = mailAdres.find(".")
        uzunlukSay = mailAdres.count(".") + 1

        if uzunlukSay != uzunluk:
            return False
        elif uzunluk > 3 or uzunluk < 1:
            return False
        elif at == -1:
            return False
        elif atCount != 1:
            return False

        for i in mailAdres[:at]:
            if kAdiKullanim.find(i) == -1:
                return False

        if uzunluk == 1:
            for i in mailAdres[at + 1:]:
                if webKullanim.find(i) == -1:
                    return False

        elif uzunluk > 1:
            for i in mailAdres[at + 1:nokta]:
                if webKullanim.find(i) == -1:
                    return False

            for i in mailAdres[nokta + 1:]:
                if noktaSonuKullanim.find(i) == -1:
                    return False

            if uzunluk == 2:
                if len(mailAdres[nokta + 1:]) != 3:
                    inputUzanti = input("Uzantınız 3 haneden farklı mı (e,h): ")
                    if inputUzanti == "e" or inputUzanti == "E":
                        pass
                    else:
                        return False

        elif uzunluk == 3:
            if len(mailAdres[nokta + 1:-3]) != 3:
                inputUzanti = input("Uzantınız 3 haneden farklı mı (e,h): ")
                if inputUzanti == "e" or inputUzanti == "E":
                    pass
                else:
                    return False

            ulkeKod = 0
            for i in mailAdres[::-1]:
                if i == ".":
                    break
                ulkeKod += 1

            if ulkeKod != 2:
                return False
    except:
        return False

    return True


try:
    print("""-------Mail Doğrulayıcı-------
Açıklama : kullaniciadi@websiteadi.uzanti.ulkekodu
Uzunluk Örnekleri:  yusufmarasel23@gazi.edu.tr (3)
                    yusufmarasel23@gazi.edu    (2)
                    yusufmarasel23@gazi        (1)\n""")
    lenUzunluk = int(input("Uzunluk ([1,3] aralığı) : "))
    mail = input("Mail adresiniz :")

    if mailDogrula(mail, lenUzunluk):
        print("\nMail adresiniz uygundur.")

    else:
        print("\nMail adresiniz uygun değildir.")

except:
    print("Hatalı Tuşlama Yaptınız !")
