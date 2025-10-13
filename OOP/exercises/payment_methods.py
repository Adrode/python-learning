from abc import ABC, abstractmethod

class PaymentMethod(ABC):
  def __init__(self, amount):
    self.amount = amount

  @abstractmethod
  def process_payment(self):
    pass

class CreditcardPayment(PaymentMethod):
  def process_payment(self):
    print(f"Payment successful. ${self.amount} processed using Credit Card method")

class PayPalPayment(PaymentMethod):
  def process_payment(self):
    print(f"Payment successful. ${self.amount} processed using PayPal method")

class BLIKPayment(PaymentMethod):
  def process_payment(self):
    print(f"Payment successful. ${self. amount} processed using BLIK method")

paypal = PayPalPayment(100)
blik = BLIKPayment(120)
credit_card = CreditcardPayment(1500)
paypal.process_payment()
blik.process_payment()
credit_card.process_payment()