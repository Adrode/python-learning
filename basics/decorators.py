main = input("Type main ice cream flavor: ")
sprinkles = input("Type sprinkles flavor: ")
icing = input("Type icing flavor: ")

def add_sprinkles(sprinkles_flavor):
  def decorator(func):
    def wrapper(*args, **kwargs):
      print(f"*You add {sprinkles_flavor} sprinkles*")
      func(*args, **kwargs)
    return wrapper
  return decorator

def add_icing(icing_flavor):
  def decorator(func):
    def wrapper(*args, **kwargs):
      print(f"*You add {icing_flavor} icing*")
      func(*args, **kwargs)
    return wrapper
  return decorator

@add_sprinkles(sprinkles)
@add_icing(icing)
def get_ice_cream(main_flavor):
  print(f"Here is your {main_flavor} ice cream")

get_ice_cream(main)