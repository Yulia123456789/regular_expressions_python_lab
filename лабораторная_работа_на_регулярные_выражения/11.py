import re

list_price = "Текст с ценами: 23.78 USD, 22 UDD, 53.95 EU, 0.002 USD, 00.02 US, 89.31 RUR, 65 RUR, 1.9 EU, 9.32 USD, 653.95 EU, 6 RUR, 239.7 USD, 05555.033 RUR,"

reg = r'(?:^|[\n\r]|[^\w\d\.])([1-9]\d*(?:.\d{,2})?\s*(?:USD|EU|RUR))\b'


d = ([x.group() for x in re.finditer(reg, list_price)])


print(d)