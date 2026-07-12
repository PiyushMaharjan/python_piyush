"""url = input("URL: ").strip()

username=url.replace("https://twitter.com/","")
print(f"Username:{username}")"""

"""""
import re

url=input("URL:").strip()

username=re.sub(r"https://twitter.com/","",url)
print(f"Username:{username}")"""
"""""
import re

url=input("URL:").strip()

matches=re.search(r"^https?://(www\.)?twitter\.com/(.+)$",url, re.IGNORECASE)
if matches:
    print(f"Username:" , matches.group(2))
"""
import re

url=input("URL:").strip()

if matches:=re.search(r"^https?://(www\.)?twitter\.com/(.+)$",url, re.IGNORECASE):

    print(f"Username:" , matches.group(2))