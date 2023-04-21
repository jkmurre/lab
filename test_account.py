from pytest import *
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('John')

    def teardown_method(self):
        del self.a1
    
    def test_init(self):
        a2 = Account('Sarah')
        assert a2.get_name() == 'Sarah'
        assert a2.get_balance() == 0 # Every instance of the get balance function should be considered a test of that function.
    
    def test_deposit(self):
        
        # Test positive input.
        assert self.a1.deposit(100) == True
        assert self.a1.get_balance() == 100 
        
        # Test negative input.
        assert self.a1.deposit(-50) == False
        assert self.a1.get_balance() == 100
        
        # Test input as zero.
        assert self.a1.deposit(0) == False
        assert self.a1.get_balance() == 100 
        
    def test_withdraw(self):
        '''
        Tests the withdraw function
        '''
        # Test positive, valid input.
        assert self.a1.deposit(100) == True
        assert self.a1.get_balance() == 100
        assert self.a1.withdraw(50) == True
        assert self.a1.get_balance() == 50
        
        # Test zero input.
        assert self.a1.withdraw(0) == False
        assert self.a1.get_balance() == 50
        
        # Test negative input.
        assert self.a1.withdraw(-5) == False
        assert self.a1.get_balance() == 50
        
        # Test positive, invalid input.
        assert self.a1.withdraw(200) == False
        assert self.a1.get_balance() == 50
        
    
