import re

password = ['C00l_Pass', 'SupperPas1', 'Cool_pass', 'C00l']

reg = r"^(?=(.*[a-z]))(?=(.*[A-Z]))(?=(.*\d))[\w]{8,}$"

for i in password:
    if re.search(reg, i):
        print(f'Надежный пароль {i}')
    else:
        print(f'Ненадежный пароль {i}')