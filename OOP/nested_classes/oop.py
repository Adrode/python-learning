class School:
  class Student:
    def __init__(self, name, grade):
      self.name = name
      self.grade = grade

    def show_student(self):
      return f"Student: {self.name}, grade: {self.grade}"
    
    def is_passing(self):
      return self.grade >= 3

  def __init__(self, name):
    self.name = name
    self.students = []

  def show_info(self):
    return f"School name: {self.name}"
  
  def add_student(self, name, grade):
    self.students.append(self.Student(name, grade))

  def list_students(self):
    for student in self.students:
      print(f"{student.show_student()} - {'Passed' if student.is_passing() else 'Failed'}")

school = School("EZN")

school.add_student("Adrian", 5)
school.add_student("Daniel", 5)
school.add_student("Patryk", 2)
school.list_students()