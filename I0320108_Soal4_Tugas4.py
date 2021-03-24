#Usia
usia = int(input("Berapa usia kamu?"))             #Masukkan usia dalam tahun
hasil_usia = (usia >= 21)

#Kelulusan
kelulusan = input("Apakah kamu sudah lulus ujian kualifikasi? (Y/T)")           #Masukkan hasil ujian dengan Y atau T
hasil_kelulusan = (kelulusan == "Y")

#Menampilkan Hasil
if hasil_usia and hasil_kelulusan :
    print("Anda dapat mendaftar di kursus")
else :
    print("Anda tidak dapat mendaftar di kursus")