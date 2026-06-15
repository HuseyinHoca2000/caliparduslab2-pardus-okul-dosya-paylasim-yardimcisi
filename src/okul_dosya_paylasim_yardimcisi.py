#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pardus Okul Dosya Paylaşım Yardımcısı
ÇalıPardusLab2 / Pardus Hata Yakalama ve Öneri Yarışması 2026

Bu ilk prototip, okul içi dosya paylaşım alanlarına erişim fikrini
sade bir menü üzerinden göstermektedir.
Gerçek ağ bağlantısı kurmaz; bilgilendirme ve simülasyon çıktıları üretir.
"""

PAYLASIM_ALANLARI = {
    "1": {
        "ad": "Öğretmen Paylaşım Alanı",
        "yol": "smb://okul-sunucusu/ogretmenler",
        "aciklama": "Öğretmenlerin ders materyali ve ortak belgeleri paylaşması için kullanılır."
    },
    "2": {
        "ad": "Öğrenci Paylaşım Alanı",
        "yol": "smb://okul-sunucusu/ogrenciler",
        "aciklama": "Öğrencilerin kendi çalışma dosyalarına ulaşması için kullanılır."
    },
    "3": {
        "ad": "Ortak Ders Materyalleri",
        "yol": "smb://okul-sunucusu/ders_materyalleri",
        "aciklama": "Tüm öğrenciler ve öğretmenler için ortak ders kaynakları alanıdır."
    },
    "4": {
        "ad": "Bilişim Laboratuvarı Paylaşımı",
        "yol": "smb://okul-sunucusu/bilisim_lab",
        "aciklama": "Bilişim dersleri için örnek kodlar, uygulamalar ve dokümanlar alanıdır."
    }
}


def baslik_yaz() -> None:
    print("=" * 70)
    print("PARDUS OKUL DOSYA PAYLAŞIM YARDIMCISI")
    print("=" * 70)
    print("Okul ağı dosya paylaşım alanları için yardımcı prototip\n")


def menu_goster() -> None:
    print("Lütfen erişmek istediğiniz paylaşım alanını seçin:")
    for kod, bilgi in PAYLASIM_ALANLARI.items():
        print(f"{kod} - {bilgi['ad']}")
    print("5 - Tüm paylaşım alanlarını göster")
    print("6 - Çıkış")
    print()


def paylasim_bilgisi_goster(secim: str) -> None:
    bilgi = PAYLASIM_ALANLARI.get(secim)

    if not bilgi:
        print("\nGeçersiz paylaşım alanı seçimi.\n")
        return

    print(f"\n[{bilgi['ad']}]")
    print(f"Bağlantı yolu: {bilgi['yol']}")
    print(f"Açıklama: {bilgi['aciklama']}")
    print("Durum: Bağlantı bilgisi gösterildi. Gerçek bağlantı kurulmadı. (simülasyon)\n")


def tum_paylasimlari_goster() -> None:
    print("\n[Tüm Paylaşım Alanları]")
    for kod, bilgi in PAYLASIM_ALANLARI.items():
        print(f"{kod} - {bilgi['ad']}")
        print(f"    Yol: {bilgi['yol']}")
        print(f"    Açıklama: {bilgi['aciklama']}")
    print()


def ana_program() -> None:
    baslik_yaz()

    while True:
        menu_goster()
        secim = input("Seçiminiz: ").strip()

        if secim in PAYLASIM_ALANLARI:
            paylasim_bilgisi_goster(secim)
        elif secim == "5":
            tum_paylasimlari_goster()
        elif secim == "6":
            print("\nDosya paylaşım yardımcısı kapatıldı.")
            break
        else:
            print("\nGeçersiz seçim yaptınız. Lütfen tekrar deneyin.\n")


if __name__ == "__main__":
    ana_program()
