def get_vowels_numbers(mot):
	counterv = 0
	counterc = 0
	for letter in mot:
		if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
			counterv += 1
	return counterv
	for letter in mot:
		if letter in ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]:
			counterc += 1
	return counterc

mot = input("Entrez un mot : ")
counterv = get_vowels_numbers(mot)
counterc = get_vowels_numbers(mot)
print("Il y a", counterv, "voyelles et", counterc, "consones dans le mot", mot)
