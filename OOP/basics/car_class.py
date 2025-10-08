class Car:
  author = "Adrian Wozniak"
  num_cars = 0

  def __init__(self, model, year, color, for_sale):
    self.model = model
    self.year = year
    self.color = color
    self.for_sale = for_sale
    Car.num_cars += 1

  def print_info(self):
    print(self.model)
    print(self.year)
    print(self.color)
    print(f"For sale?: {self.for_sale}")

  def is_car_for_sale(self):
    if self.for_sale == True:
      print("This car is for sale!")
    else:
      print("This car is not for sale.")

  def about_author(self):
    print(f"Author is: {self.author}")