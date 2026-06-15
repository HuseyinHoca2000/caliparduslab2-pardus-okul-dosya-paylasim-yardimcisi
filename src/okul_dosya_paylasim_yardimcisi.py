#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pardus Okul Dosya Paylaşım Yardımcısı
ÇalıPardusLab2 / Pardus Hata Yakalama ve Öneri Yarışması 2026
"""

import json
from pathlib import Path


VERI_DOSYASI = Path("data/paylasimlar.json")


def paylasimlari_yukle():
    try:
        with open(VERI_DOSYASI, "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    except FileNotFoundError:
        print("Hata: data/paylasimlar.json dosyası bulunamadı.")
        return []
    except json.JSONDecodeError:
        print("Hata: JSON dosyası okunamadı. Yazım hatası olabilir.")
        return []


def baslik_yaz() -> None:
    print("=" * 70)
    print("PARDUS OKUL DOSYA PAYLAŞIM YARDIMCISI")
    print("=" * 70)
    print("Okul ağı dosya paylaşım alanları için yardımcı prototip\n")


def menu_goster(paylasimlar) -> None:
    print("Lütfen erişmek istediğiniz paylaşım alanını seçin:")

    for sira, bilgi in enumerate(paylasimlar, start=1):
        print(f"{sira} - {bilgi['ad']}")

    print(f"{len(paylasimlar) + 1} - Tüm paylaşım alanlarını göster")
    print(f"{len(paylasimlar) + 2} - Çıkış")
    print()


def paylasim_bilgisi_goster(bilgi) -> None:
    print(f"\n[{bilgi['ad']}]")
    print(f"Bağlantı yolu: {bilgi['yol']}")
    print(f"Açıklama: {bilgi['aciklama']}")
    print("Durum: Bağlantı bilgisi gösterildi. Gerçek bağlantı kurulmadı.\n")


def tum_paylasimlari_goster(paylasimlar) -> None:
    print("\n[Tüm Paylaşım Alanları]")

    for sira, bilgi in enumerate(paylasimlar, start=1):
        print(f"{sira} - {bilgi['ad']}")
        print(f"    Yol: {bilgi['yol']}")
        print(f"    Açıklama: {bilgi['aciklama']}")

    print()


def ana_program() -> None:
    paylasimlar = paylasimlari_yukle()

    if not paylasimlar:
        print("Paylaşım alanı bulunamadı. Program sonlandırılıyor.")
        return

    baslik_yaz()

    while True:
        menu_goster(paylasimlar)

        secim = input("Seçiminiz: ").strip()

        if not secim.isdigit():
            print("\nLütfen sayı giriniz.\n")
            continue

        secim_no = int(secim)

        if 1 <= secim_no <= len(paylasimlar):
            paylasim_bilgisi_goster(paylasimlar[secim_no - 1])

        elif secim_no == len(paylasimlar) + 1:
            tum_paylasimlari_goster(paylasimlar)

        elif secim_no == len(paylasimlar) + 2:
            print("\nDosya paylaşım yardımcısı kapatıldı.")
            break

        else:
            print("\nGeçersiz seçim yaptınız. Lütfen tekrar deneyin.\n")


if __name__ == "__main__":
    ana_program()
