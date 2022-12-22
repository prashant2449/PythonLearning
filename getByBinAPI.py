import requests
import json

test_response = requests.get('http://preprod-payment.nyk00-int.network/payment/info/card/getByBin', params={'bin': '489377'})
assert test_response.status_code
json_response1 = test_response.json()

assert json_response1['data']['type'] == 'CC'
assert json_response1['data']['issuerBank'] == 'HDFC'
assert json_response1['data']['isInternationalCard'] == False




