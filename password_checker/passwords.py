LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

def main():
    """
    The main function of the program.
    """
    
    stop = "a"

    while stop != "quit":
        stop = input("Enter 'quit' to exit or 'continue' to check another password: ").strip().lower()
        if stop == "continue":
            password = input("Enter a password to check: ").strip()
            word_in_file(password, "toppasswords.txt", True)
            word_has_character(password, LOWER)
            word_has_character(password, UPPER)
            word_has_character(password, DIGITS)
            word_has_character(password, SPECIAL)
            word_complexity(password)
            password_strength(password, 10, 15)

        elif stop == "quit":
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please enter 'quit' or 'continue'.")
    

def word_in_file(word, filename, case_sensitive):
    """
    Check if password is a common password.
    """
    with open("passwords.txt", "r", encoding="utf-8") as password_file:
        passwords = password_file.readlines()

    pass

def word_has_character(word, character_list):
    pass

def word_complexity(word):
    pass

def password_strength(password, min_length, strong_length):
    pass


if __name__ == "__main__":
    main()