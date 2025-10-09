def is_valid_email(email):
    if "@" in email and "." in email:
            return "Valid"
    return "Invalid"
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result += ch
    return result
def get_initials(name):
    parts = name.split()
    initials = ""
    for p in parts:
        initials += p[0].upper() + "."
    return initials
def extract_year(sentence):
    words = sentence.split()
    for word in words:
        if word.isdigit() and len(word) == 4:
            return word
        if len(word) == 5 and word[:-1].isdigit() and word[-1] in ".!?":
            return word[:-1]
    return False
def is_palindrome(sentence):
    text = ""
    for ch in sentence.lower():
        if ch.isalnum():  # only letters and numbers
            text += ch
    return text == text[::-1]
