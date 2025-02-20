# 1a På Island bor det 383726 invånare och i Danmark 5961249. Skapa objekt för länderna.
# (Data från januari 2024. Avrunda befolkningen.)

#1b Lägg till en metod med namnet "print_info". Om man anropar den för Sverige-objektet ska den skriva ut:
# "I Sverige bor det 10.5 miljoner invånare". Funktionen ska använda sina egenskaper,
# så att den fungerar för de andra länderna också.

#1c Lägg till landets area som en egenskap till klassen. Använd en parameter till konstruktorn, alltså __init__ metoden.
# Ge arean ett default värde på None så att man inte måste ange arean när man skapar ett landsobjekt.

#1d Ändra i metoden "print_info" så att den skriver ut arean också, men bara om arean inte är None.

class Country:

    def __init__(self, name, pop, area=None):
        self.__name = name
        self.__population = pop
        self.__area = area

# 1c, skriver alltid ut area
#    def print_info(self):
#        print(f"I {self.__name} bor det {self.__population} miljoner invånare och arean {self.__area} km²")

#1d, skriver endast ut area om det inte är None
    def print_info(self):
        area_str = f" och arean är {self.__area}km²." if self.__area is not None else "."
        print(f"I {self.__name} bor det {self.__population} miljoner invånare"+area_str)


se = Country("Sverige", 10.5, 450295)
no = Country("Norge", 5.5)
ic = Country("Island", 0.38, 103000)
dk = Country("Danmark", 6.0)

se.print_info()
no.print_info()
ic.print_info()
dk.print_info()