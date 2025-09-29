# 16. Wyświetlenie zawartości dict w postaci "klucz - wartość", posortowane w kolejności alfabetycznej.

countries = {
  "Polska": "Warszawa",
  "Czechy": "Praga",
  "Bułgaria": "Sofia",
  "Francja": "Paryż",
  "Niemcy": "Berlin",
  "Norwegia": "Oslo",
  "Litwa": "Wilno",
  "Ukraina": "Kijów"
}

for country, capital in sorted(countries.items()):
  print(f"{country} - {capital}")