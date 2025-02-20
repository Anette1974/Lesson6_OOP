# 2a Vad gör följande kod? Fixa eventuella fel.

class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

# Dog ärver klassen Animal
class Dog(Animal):
    def make_noise(self):
   #ska vara indenterat nedan
        print("Voff!") #Dog får utskriften Voff istället för att ärva från basklassen

class Cat(Animal):
    # shelf nedan är felstavat, ska vara self
    def make_noise(self):
        super().make_noise() # Här utökas make_noise() genom att först anropa super().make_noise(), alltså föräldraklassens metod.
        print("Mjau!")

# Rooster ärver klassen Animal
class Rooster(Animal):
    def make_noise(self):
        print("Kuckeliku!")  # Rooster får utskriften Kuckeliku istället för att ärva från basklassen

# tar ett argument animal och anropar dess metod make_noise().
# sound_off() är designad för att ta ett enskilt djur, men du skickar in en lista [c, d, h],
# vilket gör att animal.make_noise() inte fungerar eftersom listor inte har en make_noise()-metod.
# ska ej vara indenterat nedan
def sound_off(animals):
    animals.make_noise()

c = Cat()
d = Dog()
h = Rooster()
#sound_off() är intryckt under Rooster, vilket gör att det blir en metod i Rooster istället för en fristående funktion.
#sound_off([c, d, h])

#korrekt kod
for animal in [c, d, h]:
    sound_off(animal)


