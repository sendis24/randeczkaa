imie = str(input("podaj imie:"))
wiek = int(input("podaj wiek:"))


if wiek < 15:
    wzrost = int(input("podaj wzrost:"))
    if wzrost > 185:
        ile_ma_rodzenstwa = int(input("rodzenstwo:"))
        print("idziemy na pierwsza randke:")
        if ile_ma_rodzenstwa < 2:
            print("wez splywaj")
elif wiek <15:
    print("dasz ig?")
else:
    print("nie bo jestem gejem")
