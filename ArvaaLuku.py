#   Arvaa luku -ohjelma. Author jpeant.
#   Ohjelma arpoo luvun 1 - 100 väliltä. Käyttäjä kysyy numeroilla onko luku oikea.
#   Ohjelma vastaa "liian pieni, lähellä mutta pieni, lähellä mutta suuri, liian suuri" ja 
#   tietenkin "oikein" jos luku on oikein.
#   Help - taulukko.

#   ToDo -list
#   random%,    loop kunnes oikea vastaus%,     lopputeksti%
#   helppi - taulukko%,     lopeta%

def tyhjiä_rivejä(luku):    # syöttää tyhjiä rivejä annetun luvun mukaisesti.
    for x in range(luku):
        print("")

def kaytto():           # syöttövirheen sattuessa pika-ohje.
    print("Käyttö: luvut 1 ja 100 väliltä ja komennot helppi ja lopeta")

def helppi():           # helppi taulukko
    tyhjiä_rivejä(1)
    print("Arvaa Luku -peli")
    kaytto()
    print("Komennot:")
    print("     1 - 100      luvut       arvattavissa olevat luvut")
    print("     helppi       komento     tämä helppi lista")
    print("     lopeta       komento     lopettaa pelin")

import random
Arvattava = random.randrange(1, 100)
arv_kerta = 8           # annetaan 8 arvaus kertaa.
voitto = False

tyhjiä_rivejä(1)
print("Tehtävänäsi on arvata luku (1 - 100) ja peli kertoo oletko lähellä (+-10), ")
print("kaukana vai oikeassa luvussa. Saat 8 kertaa arvata.")
tyhjiä_rivejä(1)
print("Ohjeet saat näkyviin kirjoittamalla helppi ja painamalla enter-näppäintä.")
print("Voit lopettaa pelin milloin tahansa kirjoittamalla lopeta.")
tyhjiä_rivejä(1)
print("Aloitetaan. Olen arponut nyt numeron ja mikä on arvauksesi?")

while arv_kerta > 0:    # pelin varsinainen looppi.
    
    try:
        tyhjiä_rivejä(1)
        Vastaus = input(">>: ")
        if Vastaus == "lopeta":
            print("Lopetetaan peli.")
            break

        elif Vastaus == "helppi":
            helppi()
   
        elif int(Vastaus) > 100 or int(Vastaus) < 1:
            kaytto()

        elif int(Vastaus) < Arvattava and int(Vastaus) >= (Arvattava - 10):
            arv_kerta = arv_kerta - 1
            print("Olet lähellä ja oikea numero on isompi. "+ str(arv_kerta) +" kertaa jäljellä." )
            
        elif int(Vastaus) < Arvattava and int(Vastaus) < Arvattava - 10:
            arv_kerta = arv_kerta - 1
            print("Olet kaukana ja oikea numero on isompi. "+ str(arv_kerta) +" kertaa jäljellä." )
            
        elif int(Vastaus) > Arvattava and int(Vastaus) <= (Arvattava + 10):
            arv_kerta = arv_kerta - 1
            print("Olet lähellä ja oikea numero on pienempi. "+ str(arv_kerta) +" kertaa jäljellä." )
            
        elif int(Vastaus) > Arvattava and int(Vastaus) > Arvattava + 10:
            arv_kerta = arv_kerta - 1
            print("Olet kaukana ja oikea numero on pienempi. "+ str(arv_kerta) +" kertaa jäljellä." )
        
        elif int(Vastaus) == Arvattava:
            arv_kerta = arv_kerta - 1
            voitto = True
            print("Loistavaa! " + str(Arvattava) + " oli oikein. Ja " + str(arv_kerta) + " arvausta jäi.")
            break

    except ValueError:      # syöttövirheen sattuessa.
        print("En ymmärrä, koita uudestaan.")
        kaytto()

if arv_kerta == 0 and voitto == False:
    print("Pahoittelen, arvaus kertasi loppuivat. Oikea numero olisi ollut " + str(Arvattava) + ".")