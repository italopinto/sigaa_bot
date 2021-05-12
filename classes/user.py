class User:
    """
    The user class representing the SIGAA user
    """
    def __init__(self):
        self.__username = None
        self.__password = None
        self.__year = None

    @property
    def name(self):
        return self.__username

    @name.setter
    def name(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year
