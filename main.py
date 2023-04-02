import json

def write_json(word):
    try:
        with open('output.txt', 'a', encoding='utf-8') as f:
            json.dump(word, f, ensure_ascii=False)
    except json.JSONDecodeError as e:
            print("Erreur lors de l'écriture :", e.msg)

def generate_words(characters, length):
    if length == 0:
        yield ""
    else:  
        for char in characters:
            for combination in generate_words(characters, length-1):
                yield char + combination

def main():
    Lettres_minuscules = "abcdefghijklmnopqrstuvwxyz"
    Lettres_majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Chiffres = "0123456789"
    Caractères_speciaux = "!@#$%^&*()_+=-}{[]|;:<>?/"

    list_caracteres = Lettres_minuscules + Lettres_majuscules + Chiffres + Caractères_speciaux
    length_word = int(input("Entrez la longueur du mot : "))
    if length_word != 0:
        for password in generate_words(list_caracteres, length_word):
            write_json(password)
            print(password)


main()
