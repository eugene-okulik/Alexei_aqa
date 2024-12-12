text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
words = text.split()
symbols = [',', '.']
fin_text = []
for i in words:
    if i[-1] in symbols:
        word = i.strip(i[-1])
        new_word = word + 'ing' + i[-1]
    else:
        new_word = i + 'ing'
    fin_text.append(new_word)
print(' '.join(fin_text))
