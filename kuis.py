import random

# Fungsi rahasia di balik semua kode
def hitung_teka_teki(kata):
    vokal = "aiueoAIUEO"
    a = sum(1 for huruf in kata if huruf in vokal)
    b = sum(1 for huruf in kata if huruf.isalpha() and huruf not in vokal)
    return a * b

# --- BANK KODE RAHASIA ---
bank_soal = {
    "Laut": hitung_teka_teki("laut"),
    "Bulan": hitung_teka_teki("bulan"),
    "Langit": hitung_teka_teki("langit"),
    "Samudra": hitung_teka_teki("samudra"),
    "Matahari": hitung_teka_teki("matahari"),
    "Bintang": hitung_teka_teki("bintang"),
    "Pelangi": hitung_teka_teki("pelangi"),
    "Bumi": hitung_teka_teki("bumi"),
    "Awan": hitung_teka_teki("awan"),
    "Galaksi": hitung_teka_teki("galaksi")
}

# Siapkan kata-kata yang akan jadi tantangan
kata_tersedia = list(bank_soal.keys())

# Pilihan respon biar gak ngebosenin
respon_benar = ["Wih, GOKIL! Kodenya emang itu.", "KEREN! Otakmu setajam silet.", "Deymn, GG King! Lanjut!"]
respon_salah = ["WKWKWK, salah total!", "Bukan gitu, Bro. Mikir lagi coba.", "Awokwokwok, ngasal ya?"]

# --- MULAI MISI ---
print("====================================")
print("+++ MISI: PEMECAH KODE SEMESTA +++")
print("====================================")
print("Hanya pikiran terpilih yang bisa melihat polanya.")
print("Buktikan kalau lo salah satunya.")
print()

# Beri petunjuk, bukan jawaban
print("Ini petunjuk awalmu, wahai calon master:")
print(">> Laut = 4")
print(">> Bulan = 6")
print("------------------------------------")

# Loop utama permainan
while True:
    if not kata_tersedia:
        print("\nANJAY, SEMUA KODE TERPECAHKAN! Lo emang master sejati. RESPEK!")
        break

    kata_soal = random.choice(kata_tersedia)
    jawaban_benar = bank_soal[kata_soal]

    print(f"\nGiliranmu! Pecahkan kode untuk: '{kata_soal}'")
    jawaban_user = input("Kode menurutmu (ketik 'nyerah' buat udahan): ")

    if jawaban_user.lower() == 'nyerah':
        print("\nYah, nyerah nih? Oke deh, payah. Sampai jumpa lagi.")
        break

    try:
        if int(jawaban_user) == jawaban_benar:
            print(f"✅ {random.choice(respon_benar)} '{kata_soal}' itu kodenya {jawaban_benar}.")
            kata_tersedia.remove(kata_soal)
        else:
            print(f"❌ {random.choice(respon_salah)}")
    except ValueError:
        print("Heh! Masukin ANGKA, bukan yang lain. Fokus dong.")