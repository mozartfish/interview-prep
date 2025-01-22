class Account:
    def __init__(self, title, balance):
        self.title = title 
        self._balance = balance
    
    def display_balance(self) -> None:
        print(f"Balance: ${self._balance}")
