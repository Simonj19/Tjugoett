#Importerar bibliotek
import random
import time

class Tjugoett:
    def __init__(self):
        self.kortlek = list(range(2, 15)) * 4  #Gångar med 4 för att få en fullständig kortlek (52st)
        self.spelare_summa: int = 0
        self.dator_summa: int = 0

    def dra_kort(self, nuvarande_summa: int) -> int:
        #Drar ett kort och returnerar dess värde, hanterar även ess-värde(1 eller 14)
        kort: int = self.kortlek.pop()
        if kort == 14:
            #Returnerar 1 eller 14 beroende på tidigare summa
            return 1 if nuvarande_summa + 14 > 21 else 14 
        else:
            return kort

    def spela_runda(self) -> None:
        # Återställer poängen och blandar kortleken med hjälp av random för varje ny runda
        self.spelare_summa: int = 0   
        self.dator_summa: int = 0
        random.shuffle(self.kortlek)

        print("Välkommen till Tjugoett!")

        #Spelarens tur
        while True:
            val: str = input("Vill du dra ett kort? (Ja/Nej): ").lower()
            if val == "ja":
                poäng: int = self.dra_kort(self.spelare_summa) #Använder metoden dra_kort() och sparar sedan värdet i variabeln poäng
                self.spelare_summa += poäng #Adderar nyss dragna poängen med totalen
                print(f"Du drog {poäng}. Total poäng: {self.spelare_summa}")
                if self.spelare_summa == 21: #Kollar om spelaren får 21, isåfall vinst direkt
                    print("Grattis! Du fick exakt 21 och har vunnit!")
                    return
                elif self.spelare_summa > 21:#Kollar ifall spelare får över 21, isåfall vinner datorn
                    print("Du har över 21. Datorn vinner!")
                    return
                else:
                    continue
            elif val == "nej":
                print("Stannar, datorns tur")
                break
            else:
                print("Ogiltigt val, vänligen skriv 'ja' eller 'nej'.")

        #Datorns tur
        while self.dator_summa < 17:
            poäng: int = self.dra_kort(self.dator_summa) #Använder metoden dra_kort() och sparar sedan värdet i variabeln poäng
            self.dator_summa += poäng #Adderar nyss dragna poängen med totalen
            print(f"Datorn drog {poäng}. Datorns total poäng: {self.dator_summa}")
            time.sleep(1.5) #Delay så att allt inte printas direkt
            if self.dator_summa == 21: #Kollar om datorn får 21, isåfall vinst direkt
                print("Datorn fick exakt 21 och vinner direkt!")
                return
            elif self.dator_summa > 21: #Kollar ifall datorn får över 21, isåfall vinner användaren
                print("Datorn har över 21. Du vinner!")
                return
            else:
                continue

        #Bestämmer vinnare
        if self.dator_summa >= self.spelare_summa:
            print("Datorn vinner!")
        else:
            print("Du vinner!")

#Funktion för huvudmeny. Använder while loop för att användaren ska kunna fortsätta spela.
def huvudmeny() -> None:
    spel = Tjugoett()

    while True:
        print("\nHuvudmeny")
        val = input("Välj ett alternativ: \n1. Spela en runda \n2. Regler \n3. Avsluta\n")
        if val == "1":
            spel.spela_runda() #Startar spelet
        elif val == "2":
            print('Tjugoett är den svenska versionen av Black Jack och spelas med målet att få en kortsumma så nära 21 som möjligt utan att överskrida den. Ess räknas som 1 eller 14, kung som 13, dam som 12, knekt som 11 och övriga kort motsvarar sitt valörvärde.')
        elif val == "3": #Stänger spelet
            print("Programmet avslutas. Ha en bra dag!")
            break
        else:
            print("Ogiltigt val. Vänligen ange 1,2 eller 3.")

# Starta huvudmenyn/spelet
huvudmeny()