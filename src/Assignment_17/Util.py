"""You are given an integer  followed by  email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.


Valid email addresses must follow these rules:

It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores .
The website name can only have letters and digits .
The extension can only contain letters .
The maximum length of the extension is .

Sample Input

3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

Sample Output
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
"""


import re


def validemail(email):
    p = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(p, email)


n = int(input())
emails = [input().strip() for _ in range(n)]
valid_emails = list(filter(validemail, emails))
valid_emails.sort()

print(valid_emails)