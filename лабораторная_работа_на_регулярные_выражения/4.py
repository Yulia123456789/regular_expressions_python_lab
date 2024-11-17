
import re
url = ['http://example.com', 'http://.example.com', 'Just Text', 'https://sub.example.com', 'http://example_.com', 'https://example.com', '//a.com', 'https://example.com#anchor', 'http://ex-.com']
pattern = re.compile(r'^(https?://)?(?:[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]\.)+[a-zA-Z]{2,}(?::\d+)?(/[^?#]*)?(\?[^#]*)?(#.*)?$')

for i in url:
    if pattern.match(i):
        print(f"{i} - Валидный URL")
    else:
        print(f"{i} - Невалидный URL")