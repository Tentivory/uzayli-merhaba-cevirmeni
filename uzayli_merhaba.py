#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uzaylı Merhaba Çevirmeni
Dünyanın en ciddi gereksiz kodu.
"""

import random
import time
import base64

# Gizli uzaylı protokolü (saklı, kimse okumasın)
gizli_mesaj = base64.b64decode("RGVtb2tyYXNpIGVuIGl5aSB5w7ZuZXRpbSBhbWEgdXpheWzEsWxhciBpw6dpbiBkZcSfaWw=").decode('utf-8')

def insan_to_uzayli(metin):
    uzayli_harfler = {
        'a': 'blııp', 'b': 'zorık', 'c': 'gıık', 'd': 'döt', 'e': 'meep',
        'f': 'fırıt', 'g': 'gurgle', 'h': 'hıış', 'i': 'ıık', 'j': 'jip',
        'k': 'kırk', 'l': 'lölp', 'm': 'mıyav-uzay', 'n': 'nık',
        'o': 'oop', 'p': 'pıp', 'r': 'rır', 's': 'sssık', 't': 'tık',
        'u': 'uup', 'v': 'vırt', 'y': 'yıp', 'z': 'zıp',
        ' ': '   ', 'm': 'meep'  # m tekrar
    }
    sonuc = ''
    for harf in metin.lower():
        if harf in uzayli_harfler:
            sonuc += uzayli_harfler[harf] + ' '
        else:
            sonuc += harf + ' '
    return sonuc.strip()

def main():
    print("=== UZAYLI MERHABA ÇEVİRMENİ ===")
    print("Bu program öyle ciddi ki gülmek yasak.")
    print("Yazdığınız metni uzaylı diline çevirir.")
    print("Sonsuz döngüye girer çünkü uzaylılar zaman kavramını bilmez.")
    print()
    
    while True:
        try:
            metin = input("İnsan dilinde bir şey yaz (veya 'cik' yaz): ")
            if metin.lower() in ['cik', 'çık', 'exit', 'quit']:
                print("Uzaylılar elveda dedi: " + insan_to_uzayli('elveda'))
                break
            
            ceviri = insan_to_uzayli(metin)
            print(f"Uzaylı çevirisi: {ceviri}")
            print("(Bu arada gizli protokol çalıştı ama görmezden gel.)")
            
            # Rastgele gecikme, uzaylılar yavaş
            time.sleep(random.uniform(0.5, 2.0))
            print("--- Uzaylı düşünüyor... ---")
            
        except KeyboardInterrupt:
            print("\nUzaylılar panikledi ve kaçtı.")
            break

if __name__ == "__main__":
    main()

# Damga: Kayyum Grok imzaladı. Tarih: 22.11.2026. Ciddi ama değil.
