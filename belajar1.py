#file phyton

print("cetak data")

a=5
b=6
c=a+b
print("nilai c = ",c)

def tambahData(a, b):
    return a+b

d = tambahData(a, b)
print ("nilai d=",d)

if(a > b):
    print("nilai a lebih besar dari b")
else:
    print("nilai b lebih besar dari a")

nilai_mahasiswa=[80,75,84,90]

#print(range(len(nilai_mahasiswa)))

#print(range(5))

for i in range(len(nilai_mahasiswa)):
    print("nilai mahasiswa =",i,"=",nilai_mahasiswa[i])

def rataNilai(nilai_a):
    jumlah = 0
    for i in range(len(nilai_a)):
        jumlah+=nilai_a[i]
    return jumlah/len(nilai_a)

print(rataNilai(nilai_mahasiswa))
