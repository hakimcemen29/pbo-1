# # Tugas ke 1

# # class Kalkulator:
# #     def __init__(self, a, b):
# #         self.a = a
# #         self.b = b

# #     def jumlah(self):
# #         return self.a + self.b

# # a = float(input("Masukkan angka pertama: "))
# # b = float(input("Masukkan angka kedua: "))

# # kalkulator1 = Kalkulator(a, b)

# # hasil = kalkulator1.jumlah()
# # print("Hasil penjumlahan:", hasil)


class HitungNilai:
    def __init__(self):
        self.nilai = 0
        self.nama = ""
        self.nim = ""

    def inputNilaiNama(self):
        self.inputNama()
        self.inputNilai()

    def inputNilai(self):
        self.nilai = float(input("Masukan Nilai : "))
        return self.nilai

    def inputNama(self):
        self.nama = input("Masukan Nama : ")
        self.nim = input("Masukan Nim : ")
        return self.nama, self.nim

    def totalNilai(self):
        if self.nilai > 100:
            return "Masukan Nilai dengan benar"
        elif self.nilai >= 80 and self.nilai <= 100:
            return "A"
        elif self.nilai >= 77 and self.nilai <= 79.99:
            return "A-"
        elif self.nilai >= 74 and self.nilai <= 76.99:
            return "B+"
        elif self.nilai >= 68 and self.nilai <= 73.99:
            return "B"
        elif self.nilai >= 65 and self.nilai <= 67.99:
            return "B-"
        elif self.nilai >= 62 and self.nilai <= 64.99:
            return "C+"
        elif self.nilai >= 56 and self.nilai <= 61.99:
            return "C"
        elif self.nilai >= 45 and self.nilai <= 55.99:
            return "D"
        else:
            return "E"

c = HitungNilai()
c.inputNilaiNama()
hasil = c.totalNilai()
print("")
print("Nama  :" ,c.nama)
print("Nim   :" ,c.nim)
print("Grade :" ,hasil)
