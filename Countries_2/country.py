# 1a På Island bor det 383726 invånare och i Danmark 5961249. Skapa objekt för länderna.
# (Data från januari 2024. Avrunda befolkningen.)

#1b Lägg till en metod med namnet "print_info". Om man anropar den för Sverige-objektet ska den skriva ut:
# "I Sverige bor det 10.5 miljoner invånare". Funktionen ska använda sina egenskaper,
# så att den fungerar för de andra länderna också.

#1c Lägg till landets area som en egenskap till klassen. Använd en parameter till konstruktorn, alltså __init__ metoden.
# Ge arean ett default värde på None så att man inte måste ange arean när man skapar ett landsobjekt.

#1d Ändra i metoden "print_info" så att den skriver ut arean också, men bara om arean inte är None.

#1e Skapa en ny metod med namnet "add_language". Den ska lägga till ett av landets officiella språk.
# (Sverige har bara ett, men Finland har två språk (svenska och finska) och Schweiz har fyra.)
# För att kunna spara ett varierande antal behöver du använda en lista.


class Country:

    def __init__(self, name, pop, area=None):
        self.__name = name
        self.__population = pop
        self.__area = area
        self.languages = []

    def set_languages(self, languages):
        self.languages = languages

    def print_info(self):

        # bygger ihop det som ska skrivas ut som en sträng, s
        s = f" * I {self.__name} bor det {self.__population} miljoner invånare"

        # 1d, skriver endast ut area om det inte är None
        if self.__area:
            s += f" med en area på {self.__area} km²"
        print(s)

        s = ""
        if len(self.languages) <1:
            s = f"   - Det finns inga språk inlagda"
        elif len(self.languages) == 1:
            s = f"   - Det officiella språket är {self.languages[0]} "
        else:
            s = self.custom_join_languages()
        print(s)

    def custom_join_languages(self):
        languages = self.languages
        initial_text = "    - De officiella språken är "
        all_except_last_language = ", ".join(languages[:-1]) #join with comma, last language excluded
        last_language = " och " +languages[-1] # last language is prefixed with "och"
        return initial_text + all_except_last_language + last_language

se = Country("Sverige", 10.5, 450295)
no = Country("Norge", 5.5)
dk = Country("Danmark", 6.0)
ic = Country("Island", 0.38, 103000)
fi = Country("Finland", 5.59, 338462)


se.set_languages(["svenska", "rövarspråket", "svengelska", "python"])
dk.set_languages(["Danska", "x", "y", "z"])
fi.set_languages(["svenska", "finska"])

se.print_info()
no.print_info()
dk.print_info()
ic.print_info()
fi.print_info()