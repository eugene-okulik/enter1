"""
# Евгений добрый день, данное решение я пришел к нему сам

x = 7

number = int(input('Putt your number'))

while number != x:
    print('Try again')
    number = int(input('Put your number'))

print('Congrats')
"""


# А вот это решение я сделал с ментором и нам обоим стало интересно что из этого правильнее в контексте данного ДЗ
y = 5

while True:
    number = int(input('Put your number'))
    if y != number:
        print('Oops try again')
    else:
        print('Congrats')
        break
