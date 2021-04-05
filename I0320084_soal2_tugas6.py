nilai =0
a = 0
while True:
    jumlah = int(input('Masukkan total bilangan yang akan anda input:'))
    for a in range(1,jumlah+1):
        nilai2 = int(input('Masukkan bilangan ke-%d :' % a))
        nilai += nilai2
        mean = nilai / jumlah
    print('rata-rata bilangan tersebut = ',mean)
    break
