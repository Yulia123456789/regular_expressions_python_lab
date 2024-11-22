import re

ip_ad = ["127.0.0.1", "255.255.255.0", "1300.6.7.8", "abc.def.gha.bcd", '0.0.0.0']


reg = r"(^(2[0-5][0-5]\.|1[0-9][0-9]\.|[1-9][0-9]\.|[0-9]\.){3})((2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])$)"


for i in ip_ad:
    if re.search(reg, i) != None:
        print(f'Правильный ip {i}')
    else:
        print(f'Неправильный ip {i}')
