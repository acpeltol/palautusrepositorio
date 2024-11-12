from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

        if len(username) < 3:
            raise UserInputError("Username must be atleast 3 chars long")
        
        if len(password) < 8:
            raise UserInputError("Username must be atleast 8 chars long")
        
        if password != password_confirmation:
            raise UserInputError("Password was not confirmed")
        
        not_onlt_chars = False

        chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
                 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z',"Å","Ä","Ö"]
        
        #chars_lower = ['a', 'b', 'c', 'd', 'e', 'f',
        #                'g', 'h', 'i', 'j', 'k',
        #                'l', 'm', 'n', 'o', 'p',
        #                'q', 'r', 's', 't', 'u',
        #                'v', 'w', 'x', 'y', 'z',"å","ä","ö"]
        
        for i in password:
            if i.upper() not in chars:
                not_onlt_chars = True

        if not_onlt_chars == False:
            raise UserInputError("Invalid password")
        



user_service = UserService()
