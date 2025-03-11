def capitalize_text(text):
    return text.title()

def count_vowels(text):
    vowels = "ioueya"
    
    # "hello world" -> h e l l o  w o r l d ->
    # counter 
    return sum(1 for char in text if char.lower() in vowels)

def reverse_string(text):
    return text[::-1]