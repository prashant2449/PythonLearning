import json
import requests
from addToBagApi_RequestBody import *

url = 'https://preprod-api.nykaa.com/cartapi/v1/item/add'
header_json = {"Content-Type": "application/json",
               "Authorization": "token 023f26d04a60459b906e19b7247330d2"}

api_res = requests.post(url, json=addBagPayload('257889', '1'), headers=header_json)
assert api_res.status_code

parsed_api_res = api_res.json()
assert parsed_api_res['statusCode'] == '200'
assert parsed_api_res['message'] == 'Product added to bag'
assert parsed_api_res['data']['displayMessage'] == 'Added to Bag'
print('****All Assertion passed****')
