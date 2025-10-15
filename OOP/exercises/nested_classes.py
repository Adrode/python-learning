class Company:
  class Employee:
    def __init__(self, name, position):
      self.name = name
      self.position = position

    def get_details(self):
      print(f"{self.name} - {self.position}")

  def __init__(self, company_name):
    self.company_name = company_name
    self.employees = []

  def add_employee(self, name, position):
    self.employees.append(self.Employee(name, position))

  def list_employees(self):
    for employee in self.employees:
      employee.get_details()

company1 = Company("Carefleet")
company2 = Company("Truck Care")

company1.add_employee("Adrian", "Mł. spec. do jakichś spraw")
company1.add_employee("Kubabuba", "St. spec. do jakichś spraw")

company2.add_employee("Holobolo", "St. spec. ds. utylizacji opon")

print(company1.company_name)
company1.list_employees()

print(company2.company_name)
company2.list_employees()