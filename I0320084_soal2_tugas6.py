nilai = input('Masukkan list bilangan yang akan dirata-rata. (ex: 1 2 3 dst) : ')
list = nilai.split(' ')
nilai2 = [int(i) for i in list]
n = 0
for angka in nilai2 :
    n += angka
    mean = n/len(nilai2)
print('Nilai rata-rata adalah = ', mean)
