LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

def main():
    """
    The main function of the program.
    """
    
    password = "a"

    while password.lower() != "q":
        password = input("Enter password: ").strip().lower()
        if password.lower() == "q":
            print("Exiting the program.")
            break
        else:
            word_in_file(password, "password_checker/toppasswords.txt", True)
            word_in_file(password, "password_checker/wordlist.txt", False)
            word_complexity(password)
            password_strength(password)
    

def word_in_file(word, filename, case_sensitive=False):
    """
    Check if password is a common password.
    """
    with open(filename, "r", encoding="utf-8") as password_file:
        passwords = password_file.readlines()
        if not case_sensitive:
            word = word.lower()

        if word in passwords and case_sensitive:
            print(f"{word} is a commonly used password and is not secure.")
            return 0
        elif word in passwords and not case_sensitive:
            print(f"{word} is a dictionary word and is not secure.")
            return 0
        else:
            return
    

def word_has_character(word, character_list):
    """
    Check if password contains a specific character.
    """
    character = list(word)
    for char in character:
        if char in character_list:
            return True
    else:
        return False
    
def word_complexity(word):
    """
    Calculates complexity value of password.
    """
    complexity_rating = 0

    if word_has_character(word, LOWER):
        complexity_rating += 1
    if word_has_character(word, UPPER):
        complexity_rating += 1
    if word_has_character(word, DIGITS):
        complexity_rating += 1
    if word_has_character(word, SPECIAL):
        complexity_rating += 1

    return complexity_rating


def password_strength(word, min_length=10, strong_length=16):
    """
    Calculate password strength.
    """
    if len(word) < min_length:
        print(f"Password is too short and is not secure.")
        return 1
    elif len(word) < strong_length:
        print(f"Password is average in length.")
        return 2
    else:
        return 5



if __name__ == "__main__":
    main()