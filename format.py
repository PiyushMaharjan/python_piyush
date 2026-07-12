"""""

name = input("whats your name?").strip()

if "," in name:
    last, first=name.split(",")
    name=f"{first} {last}"
print(f"hello, {name}")
"""

import re
name=input("whats your name?").strip()
matches=re.search(r"^(.+), (.+)$", name)
if matches:
    name=matches.group(2)+" "+matches.group(1)
    name=f"{first}{last}"
print(f"hello, {name}")