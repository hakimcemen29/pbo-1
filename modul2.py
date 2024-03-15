# print("NAMA : MUHAMMAD HAKIM")
# print("NIM  : 064002300027")
# print("")
# print("PROGRAM MENGHITUNG KELILING DAN LUAS SEGITIGA")
# print('''
#     1.Keliling
#     2.Luas
#     ''')
# pilihan = input("Masukan pilihan : ")
# if pilihan == "1":
#     a = float(input("Masukan sisi ke-1 : "))
#     b = float(input("Masukan sisi ke-2 : "))
#     c = float(input("Masukan sisi ke-3 : "))
#     hasil = a + b + c
#     print(f"keliling segitiga : {hasil} cm ")
# elif pilihan == "2":
#     a = float(input("Masukan alas : "))
#     b = float(input("Masukan tinggi : "))
#     hasil = (a * b) / 2
#     print(f"luas segita : {hasil} cm ^2 ")
# else:
#     print("Masukan pilihan dengan benar ! ")

nim = int(input("Masukan dua digit terakhir : "))
for i in range(1,50):
    if i == nim:
        continue
    print(i,end= " ")