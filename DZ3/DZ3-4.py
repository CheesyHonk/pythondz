class Wallet:
    payment_system = "MIR"  
    
    def __init__(self, name: str, currency: str):
        
        self._balance = 0  
        self.name = name
        self.currency = currency
    
    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Нужно внести положительную сумму")
        
        self._balance += amount
        print(f"Внесено {amount} {self.currency}")
    
    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Баланс должен быт положителен")
        
        if self._balance >= amount:
            self._balance -= amount
            print(f"Снято {amount} {self.currency}")
        else:
            print("Недостаточно средств")
    
    def get_balance_info(self):
        print(f"Баланс: {self._balance} {self.currency}")
    
    def close_account(self):
        self._balance = 0
        print("Кошелек закрыт")


my_wallet = Wallet("Мой кошелёк", "USD")
my_wallet.deposit(100)
my_wallet.get_balance_info()
my_wallet.withdraw(50)
my_wallet.get_balance_info()
my_wallet.withdraw(70)  
my_wallet.close_account()
my_wallet.get_balance_info()
