
text = input("Text: ")

letters = len([l for l in text if l.isalpha()])

words = 1 + len([spaces for spaces in text if spaces == ' '])

sentences = len([punctuation for punctuation in text if punctuation == '.' or punctuation == '!' or punctuation == '?'])

coleman_liau = round(0.0588 * (letters / words) * 100 - 0.296 * (sentences / words) * 100 - 15.8)

if coleman_liau < 1:
    print('Before Grade 1')
elif coleman_liau > 15:
    print('Grade 16+')
else:
    print('Grade ', coleman_liau)