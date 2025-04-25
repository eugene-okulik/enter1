person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person

print(name, last_name, city, phone, country)


x = 'результат операции: 42'

c = 'результат операции: 514'

v = 'результат работы программы: 9'

plus1 = x.index(':')
int1 = int(x[plus1+2:]) + 10
print(f'Результат операции: {int1}')

plus2 = c.index(':')
int2 = int(c[plus2+2:]) + 10
print(f'Результат операции: {int2}')

plus3 = v.index(':')
int3 = int(v[plus3+2:]) + 10
print(f'Результат операции: {int3}')


students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))
