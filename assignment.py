# You can remove 'pass' if you written code in the function 

# Exercise 1
def is_valid_email(text):
    at = False
    dot = False
    for char in text:
        if char=="@":
            at=True
        if char==".":
            dot=True
    if at==True and dot==True:
        return "Valid"
    return "Invalid"
# Exercise 2
def remove_vowels(text):
    new_str=""
    for char in text:
        if char!="a" and char!="e" and char!="o" and char!="i" and char!="u":
            new_str=new_str+char
    return new_str
# Exercise 3
def get_initials(text):
    s = text.split()
    a=s[0][0].upper()
    b=s[1][0].upper()
    return a+"."+b+"."


# Exercise 4
def extract_year(text):
    for word in text.split():
        clean_word = word.strip("!.,?")
        if clean_word.isdigit() and len(clean_word) == 4:
            return clean_word
    return False

# Exercise 5
def is_palindrome(text):
    clean_text = ""
    for char in text.lower():
        if char.isalnum():
            clean_text = clean_text + char
    return clean_text == clean_text[::-1]

