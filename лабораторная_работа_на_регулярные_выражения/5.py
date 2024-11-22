import re

hex_number = ['#FFFFFF', '#FF3421', '#00ff00', '232323', 'f#fddee', '#fd2']
reg = r"^#[0-9A-Fa-f]{6}$"

for i in hex_number:
    if re.search(reg, i):
        print(f'Правильный шестнадцатиричный идентификатор цвета {i}')
    else:
        print(f'Неправильный шестнадцатиричный идентификатор цвета {i}')