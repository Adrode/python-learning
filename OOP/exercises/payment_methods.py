from abc import ABC, abstractmethod

class PaymentMethod(ABC):
  def __init__(self, amount):
    self.amount = amount

  @abstractmethod
  def process_payment(self):
    pass

class CreditCardPayment(PaymentMethod):
  def process_payment(self):
    print(f"Payment successful. ${self.amount} processed using Credit Card method")

class PayPalPayment(PaymentMethod):
  def process_payment(self):
    print(f"Payment successful. ${self.amount} processed using PayPal method")

class BLIKPayment(PaymentMethod):
  def process_payment(self):
    print(f"Payment successful. ${self. amount} processed using BLIK method")

payments = [CreditCardPayment(100), PayPalPayment(1200), BLIKPayment(900)]

for payment in payments:
  payment.process_payment()