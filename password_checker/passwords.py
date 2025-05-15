#For the creative requirement, I have added a counter that shows the user how many passwords they have checked.

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

def main():
    """
    The main function of the program.
    """
    
    password = "a"
    count = 0

    while password.lower() != "q":
        password = input("Enter password: ").strip()
        if password.lower() == "q":
            print("Exiting the program.")
            break
        else:
            print(f"{password_strength(password)}")
            count += 1
            print(f"You have checked {count} passwords.")
    

def word_in_file(word, filename, case_sensitive=False):
    """
    Check if password is a common password.
    """
    with open(filename, "r", encoding="utf-8") as password_file:
        password_list = password_file.readlines()
        passwords = [s.replace("\n", "") for s in password_list]
        
        if not case_sensitive:
            word = word.lower()
        
        if word in passwords:
            return True
        else:
            return False
    

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


def password_strength(password, min_length=10, strong_length=16):
    """
    Calculate password strength.
    """
    strength = word_complexity(password)
    is_common_password  = word_in_file(password, "password_checker/toppasswords.txt", True)
    is_common_word = word_in_file(password, "password_checker/wordlist.txt")

    if is_common_password:
        print(f"Password is a commonly used password and is not secure.")
        return 0
    elif is_common_word:
        print(f"Password is a dictionary word and is not secure.")
        return 0
    elif len(password) < min_length:
        print(f"Password is too short and is not secure.")
        strength = 1
        return strength
    elif len(password) < strong_length:
        return strength + 1
    else:
        print(f"Password is long, length trumps complexity this is a good password.")
        return 5

if __name__ == "__main__":
    main()