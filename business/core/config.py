import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseConfig:
    """
    Class for database configuration.
    """
    def __init__(self, **kwargs):
        self.__host = kwargs.get("host", os.environ.get("DATABASE_HOST"))
        self.__port = kwargs.get("port", os.environ.get("DATABASE_PORT"))
        self.__name = kwargs.get("name", os.environ.get("DATABASE_NAME"))
        self.__user = kwargs.get("user", os.environ.get("DATABASE_USER"))
        self.__password = kwargs.get("password", os.environ.get("DATABASE_PASSWORD"))

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, value):
        self.__host = value

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        self.__port = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        self.__user = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value
