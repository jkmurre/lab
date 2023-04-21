class Account:
    def __init__(self,name:str) -> None:
        '''
        Function to initialize the object...
        :param name: Account name
        '''
        self.__account_name = name
        self.__account_balance = 0
        
    
    def deposit(self,amount:float) -> bool:
        '''
        Adds a certain amount to the account as long as the amount is greater than 0.
        :returns bool: True = transaction is good, False = transaction is bad.
        '''
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True
    
    
    def withdraw(self,amount:float) -> bool:
        '''
        Removes a certain amount from the account IF A). The amount is not greater than the account balance; B). The amount is > 0. Returns True or False based on whether or not the transaction went through.
        :returns bool: True = transaction is good, False = Transaction is bad.
        '''
        if self.__account_balance >= amount and amount > 0:
            self.__account_balance -= amount
            return True
        else:
            return False
    
    
    def get_balance(self) -> float:
        '''
        Returns the current account value.
        :returns float: the current account balance.
        '''
        return self.__account_balance 
    
    
    def get_name(self):
        return self.__account_name