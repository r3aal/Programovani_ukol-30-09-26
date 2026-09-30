import os

with open(os.sep.join(["data", "cisla.txt"]), encoding = "utf-8") as cisla:
    radky = cisla.readlines()

    if len(radky) <= 0:
        print("Soubor je prazdny")
        exit()

    max = int(radky[0].strip())
    for radek in radky:
        cislo = int(radek.strip())
        if cislo > max:
            max = cislo

    print(f"Nejvetsi cislo v souboru je: {max}")