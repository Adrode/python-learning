try:
  path = input("Podaj ścieżkę do pliku: ")
  with open(path, 'r') as f:
    print(f.read())
except FileNotFoundError:
  print("Brak takiego pliku")
except PermissionError:
  print("Brak dostępu do pliku")
finally:
  print("sic!")