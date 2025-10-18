class Temperature:
  def __init__(self, celsius):
    self._celsius = celsius

  @property
  def celsius(self):
    return f"{self._celsius} celsius"
  
  @celsius.setter
  def celsius(self, new_temp):
    self._celsius = new_temp

  @celsius.deleter
  def celsius(self):
    del self._celsius
    print("Celsius value has been deleted")


temp = Temperature(20)
print(temp.celsius)
temp.celsius = 10
print(temp.celsius)
del temp.celsius