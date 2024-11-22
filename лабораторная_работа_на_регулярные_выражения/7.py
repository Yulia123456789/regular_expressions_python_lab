import re

email = ["test@example.com", "valid_123@example.co.uk", "another.invalid@domain,com", "bug@@@com.ru", "root@localhost", 'user@example.com', "Just Text2"]

reg = r"(^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})?)$)"

for i in email:
    if re.search(reg, i):
        print(f'Правильный email {i}')
    else:
        print(f'Неправильный email {i}')