from Kalkulacka import Kalkulacka
while True:
    
    vysledek = Kalkulacka(float(input('Zadej prvni cislo:')), float(input('Zadej druhe cislo:')))


    print("Vyber:   1 = sčítání    2 = odčítání    3 = dělení    4 = násobení")
    volba = input ('Vyber operaci:')
    volba = int(volba)

    if volba == 1:
        print(vysledek.scitani())
    elif volba == 2:
        print(vysledek.odcitani())

    elif volba == 3:
        print(vysledek.deleni())

    elif volba == 4:
        print(vysledek.nasobeni())

    else:
        print("Tato volba není definována")

    konec = input("Jestliže chcete ukončit program napište konec v opačném případě stiskněte enter")
    if konec == 'konec':
        print("Program byl ukončen")
        break

print("Děkuji za použití programu :)")




