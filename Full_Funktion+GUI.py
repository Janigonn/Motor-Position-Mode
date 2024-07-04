import os
import sys
import tkinter
from colorama import Fore, Back, Style
import subprocess
def clear():
    os.system("cls")
    #os.system("clear")
def caps():
    print(Fore.BLUE +"███╗░░░███╗░█████╗░████████╗░█████╗░██████╗░  ██████╗░░█████╗░░██████╗██╗████████╗██╗░█████╗░███╗░░██╗")
    print("████╗░████║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██╔════╝██║╚══██╔══╝██║██╔══██╗████╗░██║")
    print("██╔████╔██║██║░░██║░░░██║░░░██║░░██║██████╔╝  ██████╔╝██║░░██║╚█████╗░██║░░░██║░░░██║██║░░██║██╔██╗██║")
    print("██║╚██╔╝██║██║░░██║░░░██║░░░██║░░██║██╔══██╗  ██╔═══╝░██║░░██║░╚═══██╗██║░░░██║░░░██║██║░░██║██║╚████║")
    print("██║░╚═╝░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║  ██║░░░░░╚█████╔╝██████╔╝██║░░░██║░░░██║╚█████╔╝██║░╚███║")
    print("╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░░╚════╝░╚═════╝░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝" + Style.RESET_ALL + Fore.BLUE)
    for x in range(6):
        print("")
def hex_aufteilen_und_addieren():
    try:
        # Eingabe der dezimalen Zahlen mit Validierung
        dezimal_zahlen = []
        eingabe_namen = ["ID", "MODE", "SPEED", "ACC", "POSITION"]
        grenzen = {
            "ID": (1, 9),
            "MODE": (1, 255),
            "SPEED": (1, 3000),
            "ACC": (1, 255),
            "POSITION": (1, 16777215)
        }

        for name in eingabe_namen:
            while True:
                clear()
                caps()
                zahl = int(input(f"Geben Sie die {name} ein von {grenzen[name][0]} bis {grenzen[name][1]}: "))
                if grenzen[name][0] <= zahl <= grenzen[name][1]:
                    dezimal_zahlen.append(zahl)
                    break
                else:
                    print(f"Fehler: Die Eingabe muss im Bereich {grenzen[name][0]} bis {grenzen[name][1]} liegen.")

        # Umwandeln der dezimalen Zahlen in hexadezimale Zeichenketten
        hex_zahlen = [hex(zahl)[2:].upper() for zahl in dezimal_zahlen]

        # Aufteilen der hexadezimalen Zahlen in zweistellige Teile und Zusammenfügen zu einem String
        hex_teile = []
        for idx, zahl in enumerate(hex_zahlen):
            if idx == 2:  # Für SPEED
                if len(zahl) < 4:
                    zahl = zahl.zfill(4)  # Füge führende Nullen hinzu, falls weniger als 4 Zeichen
            elif idx == 4:  # Für POSITION
                if len(zahl) < 6:
                    zahl = zahl.zfill(6)  # Füge führende Nullen hinzu, falls weniger als 6 Zeichen
            else:
                if len(zahl) % 2 != 0:
                    zahl = '0' + zahl  # Füge eine führende Null hinzu, falls ungerade Länge
            hex_teile.extend([zahl[i:i+2] for i in range(0, len(zahl), 2)])

        # Umwandeln der hexadezimalen Teile in Dezimalzahlen und Addition
        dez_summe = sum(int(teil, 16) for teil in hex_teile)

        # Das Ergebnis auf die letzten zwei Stellen begrenzen und in hexadezimal umwandeln
        hex_summe = hex(dez_summe)[-2:].upper()

        # Zusammenfügen aller aufgeteilten Hexadezimalzahlen zu einem String
        ausgabe_string = " ".join(hex_teile) + " " + hex_summe
        clear()
        caps()
        print(f"Alle aufgeteilten Hexadezimalzahlen mit der Summe: {ausgabe_string}")

    except ValueError:
        print("Fehler: Bitte geben Sie gültige dezimale Zahlen ein.")

if __name__ == "__main__":
    hex_aufteilen_und_addieren()