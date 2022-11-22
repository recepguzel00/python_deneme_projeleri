boy_giriş=float(input("boyunuzu giriniz:"))
kilo_giriş=int(input("kilonuzu giriniz:"))

BKİ_1 = kilo_giriş/(boy_giriş*boy_giriş)
print(BKİ_1)

if BKİ_1<18.5:
    print("kişi zayıf")

elif BKİ_1  >= 18.5 and BKİ_1 <25:
    print("kişi normal")
elif BKİ_1 >= 25 and BKİ_1 < 30:
    print("kişi kilolu")
else:
    print("kişi obez")