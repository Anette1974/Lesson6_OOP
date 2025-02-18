
class User:

    def __init__(self, lang, username, password):
        self.preferred_language = lang
        self.username = username
        self.__password = password

    def __str__(self):
        """Returnerar klassens innehåll i strängformat"""
        return f"User: {self.preferred_language}, {self.username}, {self.__password}"


    def get_password(self):
        return self.__password

    #def set_password(self, ):

# Ett alternativ är att skapa en "getter" med dekoratorn @property
    @property
    def password(self):
        print("Nu anropas 'password' getter")
        return self.__password

    def is_correct_login(self, username, password):
        if username == self.username and password == self.__password:
            return True
        else:
            return False