vize1=int(input("vize 1 giriniz:"))
vize2 = int(input("vize 2 giriniz"))
final= int(input("final sınav puanınızı giriniz "))

BN=(vize1*0.30+vize2*0.30+final*0.40)
print(BN)
if   BN >=  90:
 print("AA")
elif    BN >=  85: 
 print ("BA")
elif   BN >=  80:
  print ("BB")
elif   BN >=  75:
  print ("CB")
elif   BN >=  70:
  print ("CC")
elif   BN >=  65:
  print ("DC")
elif   BN >=  60:
  print ("DD")
elif   BN >=  55:
  print ("FD")
else: 
  print ("FF")

if BN>=70:
  print("öğrenci sınıfı geçti")
elif BN<=69:
  print("öğrenci sınıftan kaldı")



