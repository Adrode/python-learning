class User:
  def __init__(self, name, mail, age):
    self.name = name
    self.mail = mail
    self.age = age

  def print_info(self):
    print(self.name)
    print(self.mail)
    print(self.age)

  def is_male(self):
    return self.name[-1:] != 'a'

user = User(name='Adrian', mail='aw@mail.com', age=25)

user.print_info()
print(user.is_male())