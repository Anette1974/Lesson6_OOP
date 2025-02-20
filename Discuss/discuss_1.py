# Discuss, övning 1

class SafeStorage:
    __data = None
    def get (self):
        return self.__data
    def put (self, data):
        self.__data = data

safe = SafeStorage()
safe.put("Anakonda") # strängen Anakonda sparas i data egenskapen i objektet
x = safe.get() # hämtar ut strängen Anakonda och sparar den i variabeln x
safe.put("Boaorm") # strängen Boaorm sparas istället för Anakonda i data egenskapen i objektet
y = safe.get() # # hämtar ut strängen Boaorm och sparar den i variabeln y
#skriver ut Anakonda Boaorm
print (x, y)
