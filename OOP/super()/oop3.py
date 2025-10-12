class Message:
  def __init__(self, text):
    self.text = text

  def print_info(self):
    print(f"Message info: {self.text}")
  
class Success(Message):
  def print_info(self):
    super().print_info()
    print(f"Message has been sent")

message = Success("kopara")
message.print_info()