# 13. Na podstawie listy, która ma 10 stringów, program ma stworzyć drugą listę która zawiera tylko słowa, które składają się z 5ciu znaków

strings = ["kappa", "throttle", "żabka", "bocian", "deszczyk", "pieprzyk", "hołota", "klasa", "Gołota", "money"]
choosen_ones = []

for item in strings:
  if len(item) == 5:
    choosen_ones.append(item)

print(choosen_ones)