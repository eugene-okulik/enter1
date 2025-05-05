import random

salary_input = input('How much your pay stub check?')

check = int(salary_input)

bonus = random.choice([True, False])

orig_check = check

if bonus:
    check = random.randint(1, 5000)


print(orig_check, bonus)
print(f'${check}')

# 2 ДЗ Надеюсь все сделал правильно
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b




gen = fibonacci_generator()

targets = [5, 200, 1000, 100000]
results = {}

for i in range(1, max(targets) + 1):
    num = next(gen)
    if i in targets:
        results[i] = num

# Выводим результаты
for key in targets:
    print(f"{key}-е число Фибоначчи: {results[key]}")