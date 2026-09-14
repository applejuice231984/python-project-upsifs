import string

text = "Hello, World! Python is amainz, ** "

translator = str.maketrans('', '', string.punctuation)


clean_text = text.translate(translator)

print(clean_text)

