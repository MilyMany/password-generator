import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars):
    """Generate a random password based on user preferences."""
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator_app():
    """Main function to run the Password Generator app."""
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the length of the password (minimum 8): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
    if password:
        print("\nYour generated password is:")
        print(password)
    else:
        print("Password generation failed. Please try again.")

if __name__ == "__main__":
    password_generator_app()
