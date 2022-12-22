import requests
import json

#GET API- http://216.10.245.166/Library/GetBook.php?AuthorName=Rahul Shetty2

response = requests.get('http://216.10.245.166/Library/GetBook.php',
                        params={'AuthorName': 'Rahul Shetty2'})
print(response.status_code)
assert response.status_code == 200

print(response.headers)
assert response.headers['Access-Control-Allow-Methods'] == 'POST'
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
