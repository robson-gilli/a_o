import csv
class Card:
    def __init__(self):
        self.balance = 0.0

    def add_credit(self, credit):
        if isinstance(credit, float):
            self.balance += credit
        else:
            raise ValueError("Amount must be float")

    def add_debit(self, debit):
        if isinstance(debit, float):
            if self.balance >= debit:
                self.balance -= debit
            else:
                raise ValueError('Not enough credit!')
        else:
            raise ValueError("Amount must be float")
