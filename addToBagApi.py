import json
import requests

cart_api = requests.post('https://preprod-api.nykaa.com/cartapi/v1/item/add', json={
  "deviceType": "WEBSITE",
  "domain": "nykaa",
  "appVersion": "2.8.1",
  "store": "nykaa",
  "pro": "false",
  "items": [
    {
      "productId": "10508",
      "quantity": "1"
    }
  ],
  "customer_group_id": "11"
}, headers={"Content-Type": "application/json", "Authorization": "token 023f26d04a60459b906e19b7247330d2"})

assert cart_api.status_code
parsed_cart_response = cart_api.json()

assert parsed_cart_response['statusCode'] == '200'
assert parsed_cart_response['message'] == 'Product added to bag'
assert parsed_cart_response['data']['displayMessage'] == 'Added to Bag'
print('****All Assertion passed****')
