print("""********************
kullanıcı girşi
********************
""")
sys_kullanıcı_girişi1_="recep"
sys_kullanıcı_girişi2_="123456"


kullanıcı_girişi1=input("kullanıcı adı:")
kullanıcı_girişi2=input("kullanıcı şifre")

if (kullanıcı_girişi1==sys_kullanıcı_girişi1_ and kullanıcı_girişi2!=sys_kullanıcı_girişi2_):
 print("şifre hatalı...")
elif(kullanıcı_girişi1!=sys_kullanıcı_girişi1_ and kullanıcı_girişi2==sys_kullanıcı_girişi2_):
    print("kullanıcı adı hatalı....")
elif(kullanıcı_girişi1!=sys_kullanıcı_girişi1_ and kullanıcı_girişi2!=sys_kullanıcı_girişi2_):
    print("kullanıcı adı  ve şifre hatalı....")
else:
    print("sistme başarıyla girilmiştir....")