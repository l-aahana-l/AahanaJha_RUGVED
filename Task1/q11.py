def gradeLevel(text):
    letters = sum(c.isalpha() for c in text)
    words = len([word for word in text.split() if word])
    sentences = text.count('.') + text.count('!') + text.count('?')
    if words == 0:
        return "Text does not contain valid words"
    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    return round(index)
text = input("Enter the text:")
grade = gradeLevel(text)
print("Grade level:",grade)
