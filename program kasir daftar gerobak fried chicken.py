print("GEROBAK FRIED CHCIKEN")
print("===============================")
print("Kode Jenis   Potongan    Harga")
print("     D         Dada     Rp.2500")
print("     P         Paha     Rp.2000")
print("     S         Sayap    Rp.1500")
print("===============================")
#INPUT PROGRAM
banyak_jenis = int(input("Banyak Jenis : "))
kode_potong = []
banyak_potong = []
jenis_potong = []
harga = []
jumlah = []

i= 0
while i<banyak_jenis:
    print("Jenis Ke - ", i+1)
    kode_potong.append(input("Kode Potong [D/P/S] : "))
    banyak_potong.append(int(input("Banyak Potong : ")))

    if kode_potong[i] == "D" or kode_potong[i] == "d" :
        jenis_potong.append("Dada")
        harga.append("2500")
        jumlah.append(banyak_potong[i]*int("2500"))
    elif kode_potong[i] == "P" or kode_potong[i] == "p" :
        jenis_potong.append("Paha")
        harga.append("2000")
        jumlah.append(banyak_potong[i]*int("2000"))
    elif kode_potong[i] == "S" or kode_potong[i] == "s" :
        jenis_potong.append("Sayap")
        harga.append("1500")
        jumlah.append(banyak_potong[i]*int("1500"))
    else :
        jenis_potong.append("Kode Salah")
        harga.append("0")
        jumlah.append(banyak_potong[i]*int("0"))
    i= i + 1
    
#OUTPUT PROCESS
print("                                           ")
print("                                           ")
print("         GEROBAK FRIED CHICKEN   ")
print("===========================================")
print("No   Jenis     Harga        Banyak    Jumlah")
print("     Potong    Satuan       Beli      Harga ")
print("===========================================")
jumlah_bayar = 0
a = 0
while a < banyak_jenis:
    jumlah_bayar= jumlah_bayar + jumlah[a]
    print("%i    %s       %s        %i         %i" % (a+1,jenis_potong[a], harga[a], banyak_potong[a], jumlah[a]))
    a = a + 1
    
pajak = jumlah_bayar * 0.1 
total_bayar = jumlah_bayar + pajak
print("===========================================")
print("Jumlah bayar Rp.",jumlah_bayar)
print("Pajak 10 % Rp. ", pajak)
print("Total Bayar Rp. ", total_bayar)
uang= int(input("Nominal uang anda Rp."))
print("===========================================")
if uang >= total_bayar:
    jumlah_uang= uang - total_bayar
    print("Sisa uang anda Rp.", jumlah_uang)
    print("=================TERIMA KASIH======================")
    print("========= SELAMAT BERBELANJA KEMBALI ==============")
elif uang <= total_bayar:
    jumlah_uang= uang - total_bayar
    print("Uang anda kurang sebesar Rp. ",jumlah_uang)
