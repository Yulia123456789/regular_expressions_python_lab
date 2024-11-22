import re

str_1 = input()

reg = r"abcdefghijklmnopqrstuv18340"

if re.search(reg, str_1) != None:
    print(f'Строка правильная {str_1}')
else:
    print(f'Строка неправильная {str_1}')


