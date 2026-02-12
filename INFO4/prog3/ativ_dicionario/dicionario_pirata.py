traducao = {
    "sir": "matey",
    "hotel": "fleabag inn",
    "student": "swabbie",
    "boy": "matey",
    "madam": "proud beauty",
    "professor": "foul blaggart",
    "restaurant": "galley",
    "your": "yer",
    "excuse": "arr",
    "students": "swabbies",
    "are": "be",
    "lawyer": "foul blaggart",
    "the": "th’",
    "restroom": "head",
    "my": "me",
    "hello": "avast",
    "is": "be",
    "man": "matey"
}

frase = input("Digite uma frase em inglês: ").lower()

traduzida = []
for palavra in frase.split():
    if palavra in traducao:
        traduzida.append(traducao[palavra])
    else:
        traduzida.append(palavra)

print("Tradução para a língua dos piratas:")
print(" ".join(traduzida))
