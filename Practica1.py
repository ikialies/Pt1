import random

def adivina_numero():
    print("\n=== Joc: Adivina el Número ===")
    nAEndevinar = random.randint(1, 10)
    intents = 3
    while intents > 0:
        try:
            eleccio = int(input("Adivina un número del 1 al 10: "))
            if eleccio < 1 or eleccio > 10:
                print("Si us plau, introdueix un número entre 1 i 10.")
                continue
            if eleccio == nAEndevinar:
                print("Felicitats! Has encertat el número.")
                return
            elif eleccio < nAEndevinar:
                print("El número és més gran.")
            else:
                print("El número és més petit.")
            intents -= 1
            print(f"Et queden {intents} intents.")
        except ValueError:
            print("Si us plau, introdueix un número vàlid.")
    print(f"Has perdut. El número era {nAEndevinar}.")

def pedra_paper_tisores():
    print("\n=== Joc: Pedra, Paper, Tisores ===")
    opcions = ['pedra', 'paper', 'tisores']
    pUsuari = 0
    pOrdinador = 0

    def guanyador(usuari, ordinador):
        if usuari == ordinador:
            return "Empat!"
        elif (usuari == 'pedra' and ordinador == 'tisores') or (usuari == 'tisores' and ordinador == 'paper') or (usuari == 'paper' and ordinador == 'pedra'):
            return "Guanyes!"
        else:
            return "Perds!"

    while pUsuari < 3 and pOrdinador < 3:
        usuari = input("Tria (pedra, paper o tisores): ").lower()
        if usuari not in opcions:
            print("Opció no vàlida. Torna-ho a intentar.")
            continue
        ordinador = random.choice(opcions)
        print(f"L'ordinador ha triat: {ordinador}")
        resultat = guanyador(usuari, ordinador)
        print(resultat)
        if resultat == "Guanyes!":
            pUsuari += 1
        elif resultat == "Perds!":
            punts_ordinador += 1
        print(f"Punts: Usuari {pUsuari} - Ordinador {pOrdinador}")

    if pUsuari == 3:
        print("Has guanyat el joc!")
    else:
        print("L'ordinador ha guanyat el joc!")



def el_penjat():
    print("\n=== Joc: El Penjat ===")
    paraules = ['gato', 'casa', 'arbre', 'sol']

    paraulaSecreta = random.choice(paraules).lower()
    intents = len(paraulaSecreta) * 2
    lletresEndevinades = ['_'] * len(paraulaSecreta)
    
    def mostrar_tauler():
        print(' '.join(lletresEndevinades))

    while intents > 0 and '_' in lletresEndevinades:
        print(f"\nEt queden {intents} intents.")
        mostrar_tauler()
        lletra = input("Introdueix una lletra: ").lower()
        if len(lletra) != 1 or not lletra.isalpha():
            print("Introdueix una única lletra.")
            continue
        if lletra in paraulaSecreta:
            for i, char in enumerate(paraulaSecreta):
                if char == lletra:
                    lletresEndevinades[i] = lletra
            print(f"Correcte! La lletra '{lletra}' és a la paraula.")
        else:
            intents -= 1
            print(f"Incorrecte! La lletra '{lletra}' no és a la paraula.")
    
    if '_' not in lletresEndevinades:
        print(f"Felicitats! Has endevinat la paraula: {paraulaSecreta}")
    else:
        print(f"Has perdut. La paraula era: {paraulaSecreta}")


def menu():
    while True:
        print("\n=== Menú de Jocs ===")
        print("1. Adivina el número")
        print("2. Pedra, Paper, Tisores")
        print("3. El Penjat")
        print("4. Sortir")

        opcio = input("Selecciona un joc (1-4): ")
        
        if opcio == '1':
            adivina_numero()
        elif opcio == '2':
            pedra_paper_tisores()
        elif opcio == '3':
            el_penjat()
        elif opcio == '4':
            print("Gràcies per jugar! Adéu!")
            break
        else:
            print("Opció no vàlida. Torna-ho a intentar.")

if __name__ == "__main__":
    menu()
