import tkinter as tk
from tkinter import messagebox
import random
import time


# ============================================================
# 🌸💕 ÇİÇEK EŞLEŞTİRME MACERASI 💕🌸
# 👧 OYUNCU 1 VS OYUNCU 2
# 🏆 İLK 10 PUANA ULAŞAN KAZANIR!
# ============================================================


# ============================================================
# 🌸 ÇİÇEKLER
# ============================================================

CICEKLER = {
    1: "🌹",
    2: "🌷",
    3: "🌻",
    4: "🌼",
    5: "🌺",
    6: "🪻",
    7: "🪷",
    8: "🌸",
    9: "🏵️",
    10: "💐",
    11: "🪴",
    12: "🍀",
    13: "🌱",
    14: "🌹",
    15: "🌷",
    16: "🌼",
    17: "🌺",
    18: "🌻",
}


# ============================================================
# 🌱 SEVİYELER
# ============================================================

SEVIYELER = {

    "Kolay": [
        6, 2, 8
    ],

    "Orta": [
        7, 11, 3, 5,
        10, 15, 14, 4
    ],

    "Zor": [
        1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12
    ]
}


# ============================================================
# 🐱🐰🐼🐸 AVATARLAR
# Unicorn yok! 😛💕
# ============================================================

AVATARLAR = [
    "🐱",
    "🐰",
    "🐼",
    "🐸"
]


# ============================================================
# 😛💕 EĞLENCELİ MESAJLAR
# ============================================================

DOGRU_MESAJLARI = [

    "Yesss! 😛💕 Harika eşleştirdin!",

    "Süperrr! 🌸✨ Bir çift daha!",

    "Vaaay! 🥳🌷 Çok iyi gidiyorsun!",

    "Çiçek dedektifi iş başında! 🔎🌺",

    "Muhteşem! 😛💕",

    "Kalpler senin için atıyor! 💕💕💕",

    "Çiçek bahçesi büyüyor! 🌈🌸",

    "Bum! 💥🌺 Mükemmel eşleşme!",

    "Çiçek ustası geliyor! 🏆🌷",

    "Harika hamle! 😛✨"
]


YANLIS_MESAJLARI = [

    "Ooopss! 😛 Bu çiçekler eşleşmedi!",

    "Bir daha dene! 🌸💕",

    "Hmmmm... 🤔 Çiçekler şaşırdı!",

    "Sorun değil! 😛 Başarabilirsin!",

    "Bu sefer olmadı! 🌷💕",

    "Çiçekler saklambaç oynuyor! 🙈🌸",

    "Azıcık daha dikkat! 👀🌺"
]


# ============================================================
# 🎮 OYUN SINIFI
# ============================================================

class CicekOyunu:

    def __init__(self, pencere):

        self.pencere = pencere

        self.pencere.title(
            "🌸💕 Çiçek Eşleştirme Macerası 😛💕"
        )

        self.pencere.geometry(
            "950x850"
        )

        self.pencere.configure(
            bg="#FFF0F7"
        )

        self.pencere.resizable(
            False,
            False
        )


        # ====================================================
        # 👧 OYUNCU BİLGİLERİ
        # ====================================================

        self.oyuncular = [
            "Ayşe",
            "Betül"
        ]

        self.avatarlar = [
            "🐱",
            "🐰"
        ]


        # ====================================================
        # 🏆 PUANLAR
        # ====================================================

        self.puanlar = {
            "Ayşe": 0,
            "Betül": 0
        }


        # ====================================================
        # 🔄 SIRA
        # ====================================================

        self.sira = 0


        # ====================================================
        # 🌱 SEVİYELER
        # ====================================================

        self.seviyeler = [
            "Kolay",
            "Orta",
            "Zor"
        ]

        self.seviye_index = 0


        # ====================================================
        # 🃏 KARTLAR
        # ====================================================

        self.kart_butonlari = []

        self.kart_degerleri = []


        # ====================================================
        # 💕 SEÇİLEN KARTLAR
        # ====================================================

        self.ilk_kart = None

        self.ikinci_kart = None


        # ====================================================
        # 🔒 KART KİLİDİ
        # ====================================================

        self.kartlar_kilitli = False


        # ====================================================
        # 🌸 EŞLEŞEN KARTLAR
        # ====================================================

        self.eslesenler = []


        # ====================================================
        # 🎯 HAMLE
        # ====================================================

        self.hamle = 0


        # ====================================================
        # 🔥 SERİ
        # ====================================================

        self.seri = {
            "Ayşe": 0,
            "Betül": 0
        }


        # ====================================================
        # ⭐ BONUS
        # ====================================================

        self.bonus_puan = 0


        # ====================================================
        # ⏱️ ZAMAN
        # ====================================================

        self.baslangic_zamani = None

        self.sure = 0

        self.oyun_devam_ediyor = False


        # ====================================================
        # 🏠 ANA MENÜ
        # ====================================================

        self.ana_menu()


    # ========================================================
    # 🏠 ANA MENÜ
    # ========================================================

    def ana_menu(self):

        self.temizle()


        baslik = tk.Label(
            self.pencere,
            text="🌸💕 ÇİÇEK EŞLEŞTİRME MACERASI 💕🌸",
            font=("Arial", 30, "bold"),
            bg="#FFF0F7",
            fg="#D63384"
        )

        baslik.pack(
            pady=25
        )


        alt_baslik = tk.Label(
            self.pencere,
            text="😛💕 ÇİÇEK DOSTLARI MACERASI 💕😛",
            font=("Arial", 22, "bold"),
            bg="#FFF0F7",
            fg="#7B2CBF"
        )

        alt_baslik.pack(
            pady=5
        )


        bilgi = tk.Label(
            self.pencere,
            text=(
                "🌸 Çiçekleri eşleştir!\n\n"
                "👧 İki oyuncu sırayla oynar.\n"
                "🏆 İlk 10 puana ulaşan kazanır!\n\n"
                "🌱 Kolay → 🌿 Orta → 🌳 Zor\n\n"
                "🔥 Seri yap, bonus kazan!\n"
                "🎁 Eğlen ve çiçek ustası ol!"
            ),
            font=("Arial", 17),
            bg="#FFF0F7",
            fg="#555555"
        )

        bilgi.pack(
            pady=15
        )


        basla = tk.Button(
            self.pencere,
            text="🌸 OYUNA BAŞLA 😛💕",
            font=("Arial", 22, "bold"),
            bg="#FF69B4",
            fg="white",
            activebackground="#FF1493",
            activeforeground="white",
            padx=35,
            pady=15,
            cursor="hand2",
            command=self.oyuncu_ayarlari
        )

        basla.pack(
            pady=20
        )


        cikis = tk.Button(
            self.pencere,
            text="🚪 Çıkış",
            font=("Arial", 14, "bold"),
            bg="#E0BBE4",
            fg="#4A235A",
            padx=30,
            pady=10,
            cursor="hand2",
            command=self.pencere.destroy
        )

        cikis.pack()


    # ========================================================
    # 👧 OYUNCU AYARLARI
    # ========================================================

    def oyuncu_ayarlari(self):

        self.temizle()


        tk.Label(
            self.pencere,
            text="👧 OYUNCULARI HAZIRLAYALIM! 👧",
            font=("Arial", 28, "bold"),
            bg="#FFF0F7",
            fg="#D63384"
        ).pack(
            pady=25
        )


        # ====================================================
        # 👧 OYUNCU 1
        # ====================================================

        oyuncu1_frame = tk.Frame(
            self.pencere,
            bg="#FFF0F7"
        )

        oyuncu1_frame.pack(
            pady=10
        )


        tk.Label(
            oyuncu1_frame,
            text="👧 OYUNCU 1",
            font=("Arial", 19, "bold"),
            bg="#FFF0F7",
            fg="#7B2CBF"
        ).pack()


        tk.Label(
            oyuncu1_frame,
            text="İsmini yaz:",
            font=("Arial", 14),
            bg="#FFF0F7"
        ).pack()


        self.isim1 = tk.Entry(
            oyuncu1_frame,
            font=("Arial", 16),
            justify="center"
        )

        self.isim1.insert(
            0,
            "Ayşe"
        )

        self.isim1.pack(
            pady=5
        )


        tk.Label(
            oyuncu1_frame,
            text="Avatarını seç:",
            font=("Arial", 13),
            bg="#FFF0F7"
        ).pack()


        self.avatar1_secim = tk.StringVar(
            value="🐱"
        )


        avatar1_frame = tk.Frame(
            oyuncu1_frame,
            bg="#FFF0F7"
        )

        avatar1_frame.pack()


        for avatar in AVATARLAR:

            tk.Radiobutton(
                avatar1_frame,
                text=avatar,
                variable=self.avatar1_secim,
                value=avatar,
                font=("Arial", 25),
                bg="#FFF0F7",
                selectcolor="#FFD6E8",
                cursor="hand2"
            ).pack(
                side="left",
                padx=5
            )


        # ====================================================
        # 👧 OYUNCU 2
        # ====================================================

        oyuncu2_frame = tk.Frame(
            self.pencere,
            bg="#FFF0F7"
        )

        oyuncu2_frame.pack(
            pady=15
        )


        tk.Label(
            oyuncu2_frame,
            text="👧 OYUNCU 2",
            font=("Arial", 19, "bold"),
            bg="#FFF0F7",
            fg="#7B2CBF"
        ).pack()


        tk.Label(
            oyuncu2_frame,
            text="İsmini yaz:",
            font=("Arial", 14),
            bg="#FFF0F7"
        ).pack()


        self.isim2 = tk.Entry(
            oyuncu2_frame,
            font=("Arial", 16),
            justify="center"
        )

        self.isim2.insert(
            0,
            "Betül"
        )

        self.isim2.pack(
            pady=5
        )


        tk.Label(
            oyuncu2_frame,
            text="Avatarını seç:",
            font=("Arial", 13),
            bg="#FFF0F7"
        ).pack()


        self.avatar2_secim = tk.StringVar(
            value="🐰"
        )


        avatar2_frame = tk.Frame(
            oyuncu2_frame,
            bg="#FFF0F7"
        )

        avatar2_frame.pack()


        for avatar in AVATARLAR:

            tk.Radiobutton(
                avatar2_frame,
                text=avatar,
                variable=self.avatar2_secim,
                value=avatar,
                font=("Arial", 25),
                bg="#FFF0F7",
                selectcolor="#FFD6E8",
                cursor="hand2"
            ).pack(
                side="left",
                padx=5
            )


        # ====================================================
        # 🚀 BAŞLAT
        # ====================================================

        tk.Button(
            self.pencere,
            text="🚀 MACERAYA BAŞLA! 😛💕",
            font=("Arial", 20, "bold"),
            bg="#FF69B4",
            fg="white",
            padx=30,
            pady=12,
            cursor="hand2",
            command=self.oyunculari_kaydet
        ).pack(
            pady=15
        )


        tk.Button(
            self.pencere,
            text="🏠 Ana Menü",
            font=("Arial", 13),
            bg="#E0BBE4",
            fg="#4A235A",
            padx=25,
            pady=8,
            cursor="hand2",
            command=self.ana_menu
        ).pack()


    # ========================================================
    # 💾 OYUNCULARI KAYDET
    # ========================================================

    def oyunculari_kaydet(self):

        isim1 = self.isim1.get().strip()

        isim2 = self.isim2.get().strip()


        if isim1 == "":
            messagebox.showwarning(
                "İsim Eksik 😛",
                "Oyuncu 1 lütfen bir isim yazsın!"
            )
            return


        if isim2 == "":
            messagebox.showwarning(
                "İsim Eksik 😛",
                "Oyuncu 2 lütfen bir isim yazsın!"
            )
            return


        if isim1.lower() == isim2.lower():

            messagebox.showwarning(
                "İsimler Aynı 😛",
                "İki oyuncunun ismi farklı olsun!"
            )
            return


        self.oyuncular = [
            isim1,
            isim2
        ]


        self.avatarlar = [
            self.avatar1_secim.get(),
            self.avatar2_secim.get()
        ]


        self.oyunu_baslat()


    # ========================================================
    # 🎮 OYUNU BAŞLAT
    # ========================================================

    def oyunu_baslat(self):

        self.puanlar = {
            self.oyuncular[0]: 0,
            self.oyuncular[1]: 0
        }


        self.seri = {
            self.oyuncular[0]: 0,
            self.oyuncular[1]: 0
        }


        self.bonus_puan = 0


        self.sira = 0


        self.seviye_index = 0


        self.hamle = 0


        self.baslangic_zamani = time.time()


        self.oyun_devam_ediyor = True


        self.seviye_yukle()


    # ========================================================
    # 🌱 SEVİYE YÜKLE
    # ========================================================

    def seviye_yukle(self):

        self.temizle()


        self.ilk_kart = None

        self.ikinci_kart = None

        self.kartlar_kilitli = False

        self.eslesenler = []


        seviye = self.seviyeler[
            self.seviye_index
        ]


        cicek_listesi = SEVIYELER[
            seviye
        ]


        kart_listesi = []


        for cicek in cicek_listesi:

            kart_listesi.append(
                cicek
            )

            kart_listesi.append(
                cicek
            )


        random.shuffle(
            kart_listesi
        )


        self.kart_degerleri = kart_listesi


        # ====================================================
        # 🌸 BAŞLIK
        # ====================================================

        tk.Label(
            self.pencere,
            text=f"🌸 {seviye.upper()} SEVİYE 🌸",
            font=("Arial", 28, "bold"),
            bg="#FFF0F7",
            fg="#D63384"
        ).pack(
            pady=8
        )


        # ====================================================
        # 🏆 PUANLAR
        # ====================================================

        self.puan_etiketi = tk.Label(
            self.pencere,
            text="",
            font=("Arial", 17, "bold"),
            bg="#FFF0F7",
            fg="#7B2CBF"
        )

        self.puan_etiketi.pack(
            pady=2
        )


        # ====================================================
        # 🔥 SERİ
        # ====================================================

        self.seri_etiketi = tk.Label(
            self.pencere,
            text="",
            font=("Arial", 14, "bold"),
            bg="#FFF0F7",
            fg="#FF6B35"
        )

        self.seri_etiketi.pack(
            pady=2
        )


        # ====================================================
        # 👧 SIRA
        # ====================================================

        self.sira_etiketi = tk.Label(
            self.pencere,
            text="",
            font=("Arial", 24, "bold"),
            bg="#FFF0F7",
            fg="#E75480"
        )

        self.sira_etiketi.pack(
            pady=3
        )


        # ====================================================
        # 😛 MESAJ
        # ====================================================

        self.mesaj_etiketi = tk.Label(
            self.pencere,
            text="Çiçek arkadaşını bul! 😛💕",
            font=("Arial", 14, "bold"),
            bg="#FFF0F7",
            fg="#555555"
        )

        self.mesaj_etiketi.pack(
            pady=2
        )


        # ====================================================
        # 🃏 KART ALANI
        # ====================================================

        kart_alani = tk.Frame(
            self.pencere,
            bg="#FFF0F7"
        )

        kart_alani.pack(
            pady=8
        )


        if seviye == "Kolay":

            sutun = 3

        elif seviye == "Orta":

            sutun = 4

        else:

            sutun = 6


        self.kart_butonlari = []


        # ====================================================
        # 🃏 KARTLARI OLUŞTUR
        # ====================================================

        for i, cicek_no in enumerate(
            kart_listesi
        ):

            buton = tk.Button(
                kart_alani,
                text="❓",
                font=("Arial", 25),
                width=4,
                height=2,
                bg="#FFB6D9",
                fg="#7B2CBF",
                activebackground="#FF69B4",
                cursor="hand2",
                command=lambda
                index=i,
                no=cicek_no:
                self.karta_tikla(
                    index,
                    no
                )
            )


            satir = i // sutun

            sutun_no = i % sutun


            buton.grid(
                row=satir,
                column=sutun_no,
                padx=6,
                pady=6
            )


            self.kart_butonlari.append(
                buton
            )


        # ====================================================
        # 📊 ALT BİLGİ
        # ====================================================

        self.alt_bilgi = tk.Label(
            self.pencere,
            text="",
            font=("Arial", 12, "bold"),
            bg="#FFF0F7",
            fg="#555555"
        )

        self.alt_bilgi.pack(
            pady=3
        )


        self.bilgileri_guncelle()

        self.sure_guncelle()


    # ========================================================
    # 🃏 KARTA TIKLA
    # ========================================================

    def karta_tikla(
        self,
        index,
        cicek_no
    ):

        if self.kartlar_kilitli:

            return


        if index in self.eslesenler:

            return


        if self.ilk_kart is not None:

            if self.ilk_kart[0] == index:

                return


        # ====================================================
        # 1. KART
        # ====================================================

        if self.ilk_kart is None:

            self.ilk_kart = (
                index,
                cicek_no
            )


            self.kart_butonlari[
                index
            ].config(
                text=CICEKLER[
                    cicek_no
                ],
                bg="#FFE4F0"
            )


            self.mesaj_etiketi.config(
                text=(
                    "Şimdi çiçek arkadaşını bul! 😛💕"
                )
            )


        # ====================================================
        # 2. KART
        # ====================================================

        else:

            self.ikinci_kart = (
                index,
                cicek_no
            )


            self.kart_butonlari[
                index
            ].config(
                text=CICEKLER[
                    cicek_no
                ],
                bg="#FFE4F0"
            )


            self.hamle += 1


            self.kartlar_kilitli = True


            self.pencere.after(
                600,
                self.eslesmeyi_kontrol_et
            )


    # ========================================================
    # 💕 EŞLEŞME KONTROL
    # ========================================================

    def eslesmeyi_kontrol_et(
        self
    ):

        index1, cicek1 = self.ilk_kart

        index2, cicek2 = self.ikinci_kart


        oyuncu = self.oyuncular[
            self.sira
        ]


        # ====================================================
        # 🌸 DOĞRU EŞLEŞME
        # ====================================================

        if cicek1 == cicek2:

            self.eslesenler.append(
                index1
            )

            self.eslesenler.append(
                index2
            )


            # Seri artır
            self.seri[
                oyuncu
            ] += 1


            # Normal puan
            kazanilan = 1


            # =================================================
            # 🔥 SERİ BONUSU
            # =================================================

            if self.seri[
                oyuncu
            ] >= 3:

                kazanilan = 2

                self.bonus_puan += 1


                self.mesaj_etiketi.config(
                    text=(
                        f"🔥 ÇİÇEK ATEŞİ! 🔥\n"
                        f"{oyuncu} 2 PUAN kazandı! 😛💕"
                    )
                )

            else:

                self.mesaj_etiketi.config(
                    text=(
                        f"{random.choice(DOGRU_MESAJLARI)}\n"
                        f"🏆 +{kazanilan} PUAN!"
                    )
                )


            self.puanlar[
                oyuncu
            ] += kazanilan


            # Kartları yeşil yap
            self.kart_butonlari[
                index1
            ].config(
                bg="#B8F2C8",
                state="disabled"
            )


            self.kart_butonlari[
                index2
            ].config(
                bg="#B8F2C8",
                state="disabled"
            )


            self.bilgileri_guncelle()


            # =================================================
            # 🏆 10 PUAN KONTROL
            # =================================================

            if self.puanlar[
                oyuncu
            ] >= 10:

                self.pencere.after(
                    1000,
                    lambda:
                    self.kazanan_ekrani(
                        oyuncu
                    )
                )

                return


        # ====================================================
        # 🌷 YANLIŞ EŞLEŞME
        # ====================================================

        else:

            self.seri[
                oyuncu
            ] = 0


            self.mesaj_etiketi.config(
                text=(
                    f"{random.choice(YANLIS_MESAJLARI)}\n"
                    "🔄 Sıra değişiyor!"
                )
            )


            self.pencere.after(
                700,
                lambda:
                self.kartlari_kapat(
                    index1,
                    index2
                )
            )


            # Sıra değiştir
            self.sira = 1 - self.sira


        self.bilgileri_guncelle()


        # ====================================================
        # TÜM KARTLAR BİTTİYSE
        # ====================================================

        if len(
            self.eslesenler
        ) == len(
            self.kart_butonlari
        ):

            self.pencere.after(
                1000,
                self.sonraki_seviye
            )

            return


        self.ilk_kart = None

        self.ikinci_kart = None

        self.kartlar_kilitli = False


    # ========================================================
    # 🔄 KARTLARI KAPAT
    # ========================================================

    def kartlari_kapat(
        self,
        index1,
        index2
    ):

        self.kart_butonlari[
            index1
        ].config(
            text="❓",
            bg="#FFB6D9"
        )


        self.kart_butonlari[
            index2
        ].config(
            text="❓",
            bg="#FFB6D9"
        )


        self.ilk_kart = None

        self.ikinci_kart = None

        self.kartlar_kilitli = False


        self.bilgileri_guncelle()


    # ========================================================
    # 📊 BİLGİLERİ GÜNCELLE
    # ========================================================

    def bilgileri_guncelle(
        self
    ):

        oyuncu = self.oyuncular[
            self.sira
        ]


        self.puan_etiketi.config(
            text=(
                f"{self.avatarlar[0]} "
                f"{self.oyuncular[0]}: "
                f"{self.puanlar[self.oyuncular[0]]} 🏆"
                f"     |     "
                f"{self.avatarlar[1]} "
                f"{self.oyuncular[1]}: "
                f"{self.puanlar[self.oyuncular[1]]} 🏆"
            )
        )


        self.sira_etiketi.config(
            text=(
                f"{self.avatarlar[self.sira]} "
                f"SIRA {oyuncu.upper()}'DE 😛💕"
            )
        )


        self.seri_etiketi.config(
            text=(
                f"🔥 {oyuncu} serisi: "
                f"{self.seri[oyuncu]}"
                f"     ⭐ Bonus: "
                f"{self.bonus_puan}"
            )
        )


        if hasattr(
            self,
            "alt_bilgi"
        ):

            self.alt_bilgi.config(
                text=(
                    f"🎯 Hamle: {self.hamle}"
                    f"     |     "
                    f"🏆 Hedef: 10 puan"
                )
            )


    # ========================================================
    # ⏱️ SÜRE
    # ========================================================

    def sure_guncelle(
        self
    ):

        if self.oyun_devam_ediyor:

            if self.baslangic_zamani:

                self.sure = int(
                    time.time()
                    -
                    self.baslangic_zamani
                )


            dakika = self.sure // 60

            saniye = self.sure % 60


            self.pencere.after(
                1000,
                self.sure_guncelle
            )


    # ========================================================
    # 🌈 SONRAKİ SEVİYE
    # ========================================================

    def sonraki_seviye(
        self
    ):

        isim1 = self.oyuncular[0]

        isim2 = self.oyuncular[1]


        if (
            self.puanlar[isim1] >= 10
            or
            self.puanlar[isim2] >= 10
        ):

            return


        if self.seviye_index < 2:

            self.seviye_index += 1

            self.seviye_gecis_ekrani()

        else:

            self.final_ekrani()


    # ========================================================
    # 🎉 SEVİYE GEÇİŞ EKRANI
    # ========================================================

    def seviye_gecis_ekrani(
        self
    ):

        self.temizle()


        yeni_seviye = self.seviyeler[
            self.seviye_index
        ]


        tk.Label(
            self.pencere,
            text="🥳🎉 TEBRİKLER! 🎉🥳",
            font=("Arial", 32, "bold"),
            bg="#FFF0F7",
            fg="#D63384"
        ).pack(
            pady=40
        )


        tk.Label(
            self.pencere,
            text=(
                "🌸 Bu seviyeyi tamamladınız! 🌸\n\n"
                "Çiçek macerası devam ediyor! 😛💕"
            ),
            font=("Arial", 20, "bold"),
            bg="#FFF0F7",
            fg="#7B2CBF"
        ).pack(
            pady=20
        )


        tk.Label(
            self.pencere,
            text=(
                f"🌱 Sıradaki seviye:\n"
                f"{yeni_seviye.upper()} 🌸"
            ),
            font=("Arial", 25, "bold"),
            bg="#FFF0F7",
            fg="#E75480"
        ).pack(
            pady=20
        )


        tk.Label(
            self.pencere,
            text=(
                f"{self.avatarlar[0]} "
                f"{self.oyuncular[0]}: "
                f"{self.puanlar[self.oyuncular[0]]} puan\n"

                f"{self.avatarlar[1]} "
                f"{self.oyuncular[1]}: "
                f"{self.puanlar[self.oyuncular[1]]} puan"
            ),
            font=("Arial", 18, "bold"),
            bg="#FFF0F7",
            fg="#555555"
        ).pack(
            pady=20
        )


        tk.Button(
            self.pencere,
            text="🚀 DEVAM ET 😛💕",
            font=("Arial", 20, "bold"),
            bg="#FF69B4",
            fg="white",
            padx=30,
            pady=15,
            cursor="hand2",
            command=self.seviye_yukle
        ).pack(
            pady=25
        )


    # ========================================================
    # 🎊 KAZANAN EKRANI
    # ========================================================

    def kazanan_ekrani(
        self,
        kazanan
    ):

        self.oyun_devam_ediyor = False


        self.temizle()


        # ====================================================
        # 🎊 KUTLAMA
        # ====================================================

        tk.Label(
            self.pencere,
            text="🎉 🌸 🎊 🌷 ✨ 🪻 🎉 🌺 🎊 🌼 ✨ 💕",
            font=("Arial", 25),
            bg="#FFF0F7"
        ).pack(
            pady=25
        )


        tk.Label(
            self.pencere,
            text="🏆 KAZANAN BELLİ OLDU! 🏆",
            font=("Arial", 30, "bold"),
            bg="#FFF0F7",
            fg="#D63384"
        ).pack(
            pady=15
        )


        kazanan_index = self.oyuncular.index(
            kazanan
        )


        tk.Label(
            self.pencere,
            text=(
                f"{self.avatarlar[kazanan_index]} "
                f"🎉 TEBRİKLER {kazanan.upper()}! 🎉"
            ),
            font=("Arial", 32, "bold"),
            bg="#FFF0F7",
            fg="#FF1493"
        ).pack(
            pady=20
        )


        tk.Label(
            self.pencere,
            text=(
                "😛💕 SEN ÇİÇEK EŞLEŞTİRME "
                "ŞAMPİYONUSUN! 💕😛"
            ),
            font=("Arial", 19, "bold"),
            bg="#FFF0F7",
            fg="#7B2CBF"
        ).pack(
            pady=15
        )


        tk.Label(
            self.pencere,
            text=(
                f"🏆 {kazanan}: "
                f"{self.puanlar[kazanan]} PUAN\n\n"

                f"{self.avatarlar[0]} "
                f"{self.oyuncular[0]}: "
                f"{self.puanlar[self.oyuncular[0]]} puan\n"

                f"{self.avatarlar[1]} "
                f"{self.oyuncular[1]}: "
                f"{self.puanlar[self.oyuncular[1]]} puan\n\n"

                f"🔥 Toplam bonus: "
                f"{self.bonus_puan}\n"

                f"🎯 Toplam hamle: "
                f"{self.hamle}\n\n"

                "🌸 Harika oynadınız! 🌸\n"
                "💕😛💕😛💕"
            ),
            font=("Arial", 18, "bold"),
            bg="#FFF0F7",
            fg="#555555"
        ).pack(
            pady=15
        )


        tk.Button(
            self.pencere,
            text="🔄 TEKRAR OYNA 😛💕",
            font=("Arial", 19, "bold"),
            bg="#FF69B4",
            fg="white",
            padx=30,
            pady=15,
            cursor="hand2",
            command=self.oyuncu_ayarlari
        ).pack(
            pady=10
        )


        tk.Button(
            self.pencere,
            text="🏠 ANA MENÜ",
            font=("Arial", 14, "bold"),
            bg="#E0BBE4",
            fg="#4A235A",
            padx=30,
            pady=10,
            cursor="hand2",
            command=self.ana_menu
        ).pack(
            pady=5
        )


    # ========================================================
    # 🏁 FİNAL EKRANI
    # ========================================================

    def final_ekrani(
        self
    ):

        isim1 = self.oyuncular[0]

        isim2 = self.oyuncular[1]


        if (
            self.puanlar[isim1]
            >
            self.puanlar[isim2]
        ):

            kazanan = isim1


        elif (
            self.puanlar[isim2]
            >
            self.puanlar[isim1]
        ):

            kazanan = isim2


        else:

            # Beraberlik durumunda
            # iki oyuncuya da kutlama
            self.beraberlik_ekrani()

            return


        self.kazanan_ekrani(
            kazanan
        )


    # ========================================================
    # 🤝 BERABERLİK
    # ========================================================

    def beraberlik_ekrani(
        self
    ):

        self.oyun_devam_ediyor = False


        self.temizle()


        tk.Label(
            self.pencere,
            text="🤝🎉 BERABERE! 🎉🤝",
            font=("Arial", 32, "bold"),
            bg="#FFF0F7",
            fg="#D63384"
        ).pack(
            pady=50
        )


        tk.Label(
            self.pencere,
            text=(
                "🌸 İkiniz de harikasınız! 🌸\n\n"
                "😛💕 Gerçek çiçek ustaları sizsiniz! 💕😛"
            ),
            font=("Arial", 22, "bold"),
            bg="#FFF0F7",
            fg="#7B2CBF"
        ).pack(
            pady=30
        )


        tk.Button(
            self.pencere,
            text="🔄 TEKRAR OYNA",
            font=("Arial", 20, "bold"),
            bg="#FF69B4",
            fg="white",
            padx=30,
            pady=15,
            command=self.oyuncu_ayarlari
        ).pack(
            pady=20
        )


    # ========================================================
    # 🧹 EKRANI TEMİZLE
    # ========================================================

    def temizle(
        self
    ):

        for widget in self.pencere.winfo_children():

            widget.destroy()


# ============================================================
# 🚀 PROGRAMI BAŞLAT
# ============================================================

if __name__ == "__main__":

    pencere = tk.Tk()

    oyun = CicekOyunu(
        pencere
    )

    pencere.mainloop()