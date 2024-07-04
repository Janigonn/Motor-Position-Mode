def hex_aufteilen_und_addieren():
    try:
        # Eingabe der dezimalen Zahlen
        dezimal_zahlen = []
        eingabe_namen = ["ID", "MODE", "SPEED", "ACC", "POSITION"]

        for name in eingabe_namen:
            dezimal_zahlen.append(int(input(f"Geben Sie die {name} ein: ")))

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

        print(f"CAN Massage is: {ausgabe_string}")

    except ValueError:
        print("Bitte geben Sie gültige dezimale Zahlen ein.")

if __name__ == "__main__":
    hex_aufteilen_und_addieren()