numbers = [5, 4, 5, 4, 8, 7, 10]
uniques = []
for number in numbers:
    if number not in  uniques:
        uniques.append(number)
print(uniques)