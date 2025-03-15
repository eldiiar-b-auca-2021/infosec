from itertools import permutations, product

name = "eldiiar"
surname = "bekjan"
birth_year = "2000"
birth_date = "15062000"


words = [name, surname, birth_year, birth_date]
special_chars = ["!", "@", "#", "$", "123", "01"]


basic_combinations = set()
for i in range(1, len(words) + 1):
    for perm in permutations(words, i):
        basic_combinations.add("".join(perm))
        basic_combinations.add("".join(perm).capitalize())


advanced_combinations = set()
for word in basic_combinations:
    for special in special_chars:
        advanced_combinations.add(word + special)
        advanced_combinations.add(special + word)


with open("custom_passwords.txt", "w") as f:
    for password in basic_combinations.union(advanced_combinations):
        f.write(password + "\n")

print("Wordlist generated: custom_passwords.txt")
