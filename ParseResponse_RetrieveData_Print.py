import requests
import json

#GET API- http://216.10.245.166/Library/GetBook.php?AuthorName=Rahul Shetty2

response = requests.get('http://216.10.245.166/Library/GetBook.php',
                        params={'AuthorName': 'Rahul Shetty'})
assert response.status_code
json__response = response.json()

# Retrieve book details with ISBN RGHCC
count = 0
for i in json__response:
    if i['isbn'] == 'bcd':
        print(i)
        count += 1
print(count)
