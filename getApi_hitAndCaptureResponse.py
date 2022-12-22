import requests
import json

#GET API- http://216.10.245.166/Library/GetBook.php?AuthorName=Rahul Shetty2

response = requests.get('http://216.10.245.166/Library/GetBook.php',
                        params={'AuthorName': 'Rahul Shetty2'})
json_response = response.json()
print(json_response)
print(type(json_response))


