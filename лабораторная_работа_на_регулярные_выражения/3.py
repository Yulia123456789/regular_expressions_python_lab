import re

mac_ad = ["00:14:22:01:23:Z5", "aE:dC:cA:56:76:54", "01:23:45:67:89:Az", "001422-012345", "00:14:22:01:23:45", "00:00:00:00:00:00"]

reg = r'([0-9A-Fa-f]{2}\:){5}([0-9A-Fa-f]{2})$'

for i in mac_ad:
    if re.search(reg, i) != None:
        print(f'Правильный MAC-адрес {i}')
    else:
        print(f'Неправильный MAC-адрес {i}')