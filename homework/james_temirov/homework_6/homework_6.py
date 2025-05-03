text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero.')

new_text = text.split()
text_ing = []

for word in new_text:
    if word[-1] == ',' or word[-1] == '.':
        base = word[:-1]
        punctuation = word[-1]
    else:
        base = word
        punctuation = '' 
        
    new_line = base + 'ing' + punctuation
    text_ing.append(new_line)

word_ing = ' '.join(text_ing)
print(word_ing)
