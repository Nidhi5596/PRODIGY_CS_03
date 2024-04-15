import re

def assess_password_strength(password):
   
    length_score = len(password) >= 8
    uppercase_score = any(char.isupper() for char in password)
    lowercase_score = any(char.islower() for char in password)
    digit_score = any(char.isdigit() for char in password)
    special_char_score = bool(re.search(r'[!@#$%^&*()\-_=+{};:,<.>/?[\]\'\"\\|`~]', password))

    overall_score = sum([length_score, uppercase_score, lowercase_score, digit_score, special_char_score])

    if overall_score == 5:
        return "Very Strong"
    elif overall_score == 4:
        return "Strong"
    elif overall_score == 3:
        return "Moderate"
    elif overall_score == 2:
        return "Weak"
    elif overall_score == 1:
        return "Very Weak"
    else:
        return "Password does not meet minimum criteria"

password = input("Enter your password: ")
strength = assess_password_strength(password)
print("Password Strength:", strength)
