class CPU:
  def __init__(self, cores):
    self.cores = cores

class RAM:
  def __init__(self, size):
    self.size = size

class Laptop:
  def __init__(self, cpu_cores, ram_size):
    self.cpu = CPU(cpu_cores)
    self.ram = RAM(ram_size)

  def specs_info(self):
    return f"CPU Cores: {self.cpu.cores}, RAM Size: {self.ram.size}GB"

  def update_ram(self, new_size):
    if new_size > 0:
      self.ram.size = new_size
    else:
      print("RAM size must be greater than 0")

laptop1 = Laptop(4, 8)
laptop2 = Laptop(8, 32)

print(laptop1.specs_info())
print(laptop2.specs_info())

laptop1.update_ram(0)
laptop1.update_ram(16)
print(laptop1.specs_info())