"""email = input("whats your email?").strip()

username, domain = email.split("@")

if username and  domain.endswith(".edu"):
    print("valid")

else:
    print("invalid")
"""
import re

email = input("whats your email?").strip()

if re.search(r".+@.+\.edu", email):
    print("valid")
else:
    print("invalid ")