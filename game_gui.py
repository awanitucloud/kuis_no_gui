import tkinter as tk
from tkinter import font as tkfont
import random

# --- FUNGSI LOGIKA UTAMA (Tidak berubah dari versi konsol) ---
def hitung_teka_teki(kata):
    vokal = "aiueoAIUEO"
    a = sum(1 for huruf in kata if huruf in vokal)
    b = sum(1 for huruf in kata if huruf.isalpha() and huruf not in vokal)
    return a * b

# --- KELAS UTAMA UNTUK APLIKASI GUI ---
class GameGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- DATA & STATE PERMAINAN ---
        self.bank_soal = {
            "Laut": hitung_teka_teki("laut"), "Bulan": hitung_teka_teki("bulan"),
            "Langit": hitung_teka_teki("langit"), "Samudra": hitung_teka_teki("samudra"),
            "Matahari": hitung_teka_teki("matahari"), "Bintang": hitung_teka_teki("bintang"),
            "Pelangi": hitung_teka_teki("pelangi"), "Bumi": hitung_teka_teki("bumi"),
            "Awan": hitung_teka_teki("awan"), "Galaksi": hitung_teka_teki("galaksi")
        }
        self.kata_tersedia = list(self.bank_soal.keys())
        self.respon_benar = ["Wih, GOKIL!", "KEREN! Otakmu setajam silet.", "Deymn, GG King!"]
        self.respon_salah = ["WKWKWK, salah total!", "Bukan gitu, Bro. Mikir lagi.", "Awokwokwok, ngasal ya?"]
        
        self.kata_sekarang = None
        self.jawaban_benar = None

        # --- PENGATURAN JENDELA UTAMA ---
        self.title("Pemecah Kode Semesta")
        self.geometry("400x450")
        self.resizable(False, False)
        self.configure(bg="#2d3436")

        # --- MEMBUAT SEMUA WIDGET (Tombol, Label, dll.) ---
        self.buat_widget()
        
        # --- MEMULAI PERMAINAN ---
        self.mulai_babak_baru()

    def buat_widget(self):
        # Definisikan style font
        font_judul = tkfont.Font(family="Consolas", size=18, weight="bold")
        font_biasa = tkfont.Font(family="Arial", size=11)
        font_soal = tkfont.Font(family="Arial", size=16, weight="bold")
        font_status = tkfont.Font(family="Arial", size=12, weight="bold")

        # Frame utama untuk padding
        main_frame = tk.Frame(self, bg="#2d3436", padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)

        # --- WIDGET HEADER ---
        tk.Label(main_frame, text="MISI: PEMECAH KODE SEMESTA", font=font_judul, bg="#2d3436", fg="#00cec9").pack(pady=(0, 5))
        tk.Label(main_frame, text="Hanya pikiran terpilih yang bisa melihat polanya.", font=font_biasa, bg="#2d3436", fg="white").pack()
        
        # --- WIDGET CONTOH ---
        frame_contoh = tk.Frame(main_frame, bg="#2d3436", pady=15)
        frame_contoh.pack()
        tk.Label(frame_contoh, text="Petunjuk Awal:", font=font_biasa, bg="#2d3436", fg="white").pack()
        tk.Label(frame_contoh, text=">> Laut = 4  |  Bulan = 6 <<", font=font_biasa, bg="#2d3436", fg="#fdcb6e").pack()

        # --- WIDGET PERTANYAAN ---
        self.label_soal = tk.Label(main_frame, text="Pecahkan kode untuk:", font=font_biasa, bg="#2d3436", fg="white", pady=10)
        self.label_soal.pack()

        self.label_kata = tk.Label(main_frame, text="'...'", font=font_soal, bg="#2d3436", fg="#55efc4", pady=10)
        self.label_kata.pack()

        # --- WIDGET INPUT & TOMBOL ---
        self.entry_jawaban = tk.Entry(main_frame, font=font_soal, justify="center", width=10)
        self.entry_jawaban.pack(pady=10)
        self.entry_jawaban.bind("<Return>", self.cek_jawaban) # Bind tombol Enter

        self.tombol_cek = tk.Button(main_frame, text="Cek Kode", font=font_biasa, command=self.cek_jawaban, bg="#0984e3", fg="white", relief="flat")
        self.tombol_cek.pack(pady=10, ipadx=10, ipady=4)

        # --- WIDGET STATUS/FEEDBACK ---
        self.label_status = tk.Label(main_frame, text="Selamat datang, pemecah kode!", font=font_status, bg="#2d3436", fg="white", pady=20)
        self.label_status.pack()

    def mulai_babak_baru(self):
        # Reset input dan status
        self.entry_jawaban.delete(0, tk.END)
        self.label_status.config(text="")

        if not self.kata_tersedia:
            # Jika soal habis
            self.label_kata.config(text="MISSION COMPLETE!")
            self.label_status.config(text="RESPEK! Semua kode terpecahkan!", fg="#fdcb6e")
            self.entry_jawaban.config(state="disabled")
            self.tombol_cek.config(state="disabled")
            return

        # Pilih kata baru secara acak
        self.kata_sekarang = random.choice(self.kata_tersedia)
        self.jawaban_benar = self.bank_soal[self.kata_sekarang]
        
        # Update label pertanyaan
        self.label_kata.config(text=f"'{self.kata_sekarang}'")

    def cek_jawaban(self, event=None): # event=None untuk handle tombol Enter
        jawaban_user = self.entry_jawaban.get()
        
        try:
            jawaban_int = int(jawaban_user)
            if jawaban_int == self.jawaban_benar:
                # Jika jawaban benar
                self.kata_tersedia.remove(self.kata_sekarang)
                pesan = f"✅ {random.choice(self.respon_benar)}"
                self.label_status.config(text=pesan, fg="#55efc4")
                # Lanjut ke babak berikutnya setelah 1.5 detik
                self.after(1500, self.mulai_babak_baru)
            else:
                # Jika jawaban salah
                pesan = f"❌ {random.choice(self.respon_salah)}"
                self.label_status.config(text=pesan, fg="#ff7675")
                # Hapus input yang salah agar user bisa coba lagi
                self.entry_jawaban.delete(0, tk.END)
        except ValueError:
            # Jika input bukan angka
            self.label_status.config(text="Heh! Masukin ANGKA, bukan yang lain.", fg="#fab1a0")

# --- Jalankan Aplikasi ---
if __name__ == "__main__":
    app = GameGUI()
    app.mainloop()