class PasswordManager:
    def __init__(self, password):
        self.__password = password
    
    # TODO: Implement the verify_password method
    def verify_password(self, password):
        return self.__password == password