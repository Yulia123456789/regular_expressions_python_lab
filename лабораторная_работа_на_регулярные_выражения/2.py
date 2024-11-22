import re

guid_str = ["123e4567-e89b-12d3-a456-426614174000", "{a4b3c2d1-9f8e-7d6c-5b4a-3d2e1f0c9b8a}", "e02fd0e400fd090Aca300d00a0038ba0", "e02fd0e4-00fd-090A-ca30-0d00a0038ba0", "{12345-6789-4abc-def1-23456789abcd}"]

reg = r"[0-9A-Fa-f]{8}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{12}"

reg1 = r"{[0-9A-Fa-f]{8}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{12}}"
for i in guid_str:
    if re.search(reg, i) != None or re.search(reg1, i) != None:
        print(f'Правильно {i}')
    else:
        print(f'Неправильно {i}')