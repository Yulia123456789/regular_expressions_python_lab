import re

number = ['123456', '234567', '1234567', '12345', '076745', '0000000']

reg = r'^[1-9]\d{5}$'

for i in number:
    if re.search(reg, i):
        print(f'Шестизначное {i}')
    else:
        print(f'НЕ шестизначное {i}')
