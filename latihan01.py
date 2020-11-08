

**nama : irsyanta bagus** <br>
**kelas : TI.20.A1.** <br>
**nim : 312010409**


------------------------------------------------------------------------------------------------------------------

Pada pertemuan 7 tugas PPT ke-2 ini, saya diberikan beberapa tugas oleh dosen saya yaitu

![fotopy](foto/py.png)

untuk mencari sebuah nilai maksimal dari 3 data yang sebelumnya telah diinput, dan setelah mendapat
nilai maksimalnya, dirubah menjadi dalam sebuah bentuk flowchart.

TUGAS PRAKTIKUM 2
MENGINPUT DATA DAN MENCARI NILAI MAX

Pertama-tama disini saya akan mencoba untuk menginput 3 data dengan menggunakan syntax berikut terlebih dahulu.

Masukan syntax tersebut dengan angka yang kalian inginkan.

a = int(input("Masukkan bilangan 1: "))
b = int(input("Masukkan bilangan 2: "))
c = int(input("Masukkan bilangan 3: "))


![fotopy](foto/py1.png)

Jika sudah mendapat tampilan seperti gambar diatas, maka kalian sudah berhasil menginput
ketiga data tersebut.

Langkah selanjutnya adalah mencari tahu nilai terbesar (max) dari ketiga data tersebut. Sebelum memulainya kalian harus
memasukan terlebih dahulu berapa jumlah data yang akan kalian kerjakan dari ketiga data tersebut dengan syntax

N=int(input("banyaknya data = "))


Karena disini saya diberi tugas mencari nilai max dari ketiga data maka saya akan menggunkan semua data diatas.

if N>0:
    i=1
    x=int(input("data ke -"+str(i)+"="))
    max=x;total=x
    for i in range(2,N+1):
        x=int (input("data ke -"+str(i)+"="))
        total+=x
        if max<x:
            max=x

    print("bilangan terbesar =",max)

![fotopy](foto/py2.png)

Di tugas ke dua, saya diminta untuk mencari nilai acak yang bernominal dibawah 0,5. Maka saya memasukan syntax:

import random
print(40*"=")
print("Bilangan random yang lebih kecil dari 0,5")
print(40*"=")
jum = int( input("Masukan nilai n : "))
i = 0
for i in range(jum):
    i += 1
    angkaDec = random.uniform(0, 0.5)
    print("Data ke", i, " = ", angkaDec)

Syntax dibawah ini digunakan untuk mencari nilai random

import random

Sementara untuk menentukan jumlah input yang diinginkan maka perlu memasukan

jum = int( input("Masukan nilai n : "))
dan untuk menampilkan urutan data sesuai jumlah inputan dengan hasil di bawah 0.5 perlu memasukan

angkaDec = random.uniform(0, 0.5)
    print("Data ke", i, " = ", angkaDec)

    ##terima kasih
    

