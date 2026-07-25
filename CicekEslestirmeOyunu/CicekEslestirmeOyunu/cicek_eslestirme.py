import tkinter as tk
import random
import time


# ============================================================
# 🌸💕 ÇİÇEK EŞLEŞTİRME MACERASI 💕🌸
# 👧 AYŞE VS BETÜL 👧
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
    15: "🌷"
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
# 😛💕 EĞLENCELİ MESAJLAR
# ============================================================

DOGRU_MESAJLARI = [

    "Yesss! 😛💕 Harika eşleştirdin!",

    "Süperrr! 🌸✨ Bir çift daha!",

    "Vaaay! 🥳🌷 Çok iyi gidiyorsun!",

    "Çiçek dedektifi iş başında! 🕵️🌺",

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
# 🎮 ANA OYUN SINIFI
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
        # 👧 OYUNCULAR
        # ====================================================

        self.oyuncular = [
            "Ayşe",
            "Betül"
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
        # 🌸 EŞLEŞENLER
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
        # ⭐ TOPLAM BONUS
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


        tk.Label(

            self.pencere,

            text="🌸💕 ÇİÇEK EŞLEŞTİRME MACERASI 💕🌸",

            font=("Arial", 30, "bold"),

            bg="#FFF0F7",

            fg="#D63384"

        ).pack(

            pady=30

        )


        tk.Label(

            self.pencere,

            text="😛💕 AYŞE VS BETÜL 💕😛",

            font=("Arial", 24, "bold"),

            bg="#FFF0F7",

            fg="#7B2CBF"

        ).pack(

            pady=10

        )


        tk.Label(

            self.pencere,

            text=(

                "🌸 Çiçekleri eşleştir!\n\n"

                "👧 Ayşe ve Betül sırayla oynar.\n"

                "🏆 İlk 10 puana ulaşan kazanır!\n\n"

                "🌱 Kolay → 🌿 Orta → 🌳 Zor\n\n"

                "🔥 Seri yap, bonus kazan!\n"

                "🎁 Sürpriz bonusları yakala!"

            ),

            font=("Arial", 17),

            bg="#FFF0F7",

            fg="#555555"

        ).pack(

            pady=20

        )


        tk.Button(

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

            command=self.oyunu_baslat

        ).pack(

            pady=15

        )


        tk.Button(

            self.pencere,

            text="🚪 Çıkış",

            font=("Arial", 14, "bold"),

            bg="#E0BBE4",

            fg="#4A235A",

            padx=30,

            pady=10,

            cursor="hand2",

            command=self.pencere.destroy

        ).pack()


    # ========================================================
    # 🎮 OYUNU BAŞLAT
    # ========================================================

    def oyunu_baslat(self):

        self.puanlar = {

            "Ayşe": 0,

            "Betül": 0
        }


        self.seri = {

            "Ayşe": 0,

            "Betül": 0
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


        # Her çiçekten 2 tane
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

            pady=10

        )


        # ====================================================
        # 🏆 PUAN
        # ====================================================

        self.puan_etiketi = tk.Label(

            self.pencere,

            text="",

            font=("Arial", 17, "bold"),

            bg="#FFF0F7",

            fg="#7B2CBF"

        )

        self.puan_etiketi.pack(

            pady=3

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

            pady=3

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

            pady=5

        )


        # ====================================================
        # 😛 MESAJ
        # ====================================================

        self.mesaj_etiketi = tk.Label(

            self.pencere,

            text="Çiçek arkadaşını bul! 😛💕",

            font=("Arial", 15, "bold"),

            bg="#FFF0F7",

            fg="#555555"

        )

        self.mesaj_etiketi.pack(

            pady=3

        )


        # ====================================================
        # 🃏 KART ALANI
        # ====================================================

        kart_alani = tk.Frame(

            self.pencere,

            bg="#FFF0F7"

        )

        kart_alani.pack(

            pady=10

        )


        # Sütun
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

            font=("Arial", 13, "bold"),

            bg="#FFF0F7",

            fg="#555555"

        )

        self.alt_bilgi.pack(

            pady=5

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
        # 🌸 DOĞRU
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


            # Temel puan
            kazanilan = 1


            # =================================================
            # 🔥 SERİ BONUSU
            # =================================================

            if self.seri[

                oyuncu

            ] >= 3:

                kazanilan += 1

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
        # 🌷 YANLIŞ
        # ====================================================

        else:

            # Seri sıfırla
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
        # TÜM KARTLAR BİTTİ
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
    # 📊 BİLGİLER
    # ========================================================

    def bilgileri_guncelle(

        self

    ):

        oyuncu = self.oyuncular[

            self.sira

        ]


        self.puan_etiketi.config(

            text=(

                f"👧 Ayşe: "

                f"{self.puanlar['Ayşe']} 🏆"

                f"     "

                f"👧 Betül: "

                f"{self.puanlar['Betül']} 🏆"

            )

        )


        self.sira_etiketi.config(

            text=(

                f"🌸 SIRA "

                f"{oyuncu.upper()}"

                f"'DE 😛💕"

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

                    f"🎯 Hamle: "

                    f"{self.hamle}"

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


            if hasattr(

                self,

                "alt_bilgi"

            ):

                mevcut = self.alt_bilgi.cget(

                    "text"

                )


                self.alt_bilgi.config(

                    text=(

                        mevcut

                        +

                        f"     |     ⏱️ "

                        f"{dakika:02d}:"

                        f"{saniye:02d}"

                    )

                )


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

        if (

            self.puanlar["Ayşe"]

            >= 10

            or

            self.puanlar["Betül"]

            >= 10

        ):

            return


        if self.seviye_index < 2:

            self.seviye_index += 1

            self.seviye_gecis_ekrani()

        else:

            self.final_ekrani()


    # ========================================================
    # 🎉 SEVİYE GEÇİŞ
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

                f"👧 Ayşe: "

                f"{self.puanlar['Ayşe']} puan\n"

                f"👧 Betül: "

                f"{self.puanlar['Betül']} puan"

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
    # 🏆 KAZANAN EKRANI
    # ========================================================

    def kazanan_ekrani(

        self,

        kazanan

    ):

        self.oyun_devam_ediyor = False


        self.temizle()


        # 🎊 Konfeti
        konfeti = (

            "🎉 🌸 🎊 🌷 ✨ 🪻 "

            "🎉 🌺 🎊 🌼 ✨ 💕"

        )


        tk.Label(

            self.pencere,

            text=konfeti,

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


        tk.Label(

            self.pencere,

            text=(

                f"🎉 TEBRİKLER "

                f"{kazanan.upper()}! 🎉"

            ),

            font=("Arial", 34, "bold"),

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

                f"👧 Ayşe: "

                f"{self.puanlar['Ayşe']} puan\n"

                f"👧 Betül: "

                f"{self.puanlar['Betül']} puan\n\n"

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

            command=self.oyunu_baslat

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
    # 🏁 SON EKRAN
    # ========================================================

    def final_ekrani(

        self

    ):

        if (

            self.puanlar["Ayşe"]

            >

            self.puanlar["Betül"]

        ):

            kazanan = "Ayşe"


        elif (

            self.puanlar["Betül"]

            >

            self.puanlar["Ayşe"]

        ):

            kazanan = "Betül"


        else:

            kazanan = "Berabere"


        self.kazanan_ekrani(

            kazanan

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