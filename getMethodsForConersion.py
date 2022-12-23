import requests
import json

json_response = requests.get('http://preprod-payment.nyk00-int.network/payment/info/availablePaymentMethodsForConversion',
             params={'deviceType': 'MSITE', 'domain': 'nykaa'})
assert json_response.status_code
print('****STATUS CODE****')
print(json_response.status_code, '\n')

print('****HEADER****')
print(json_response.headers, '\n')

print('****API RESPONSE****')
parsed_json_response = json_response.json()
print(parsed_json_response, '\n')

assert parsed_json_response['statusCode'] == '200'
print('****STATUS CODE ASSERTION PASSED****')

assert parsed_json_response['data'] == ['upi_intent', 'cc', 'nb', 'upi']
print('****PAYMENT MODES ASSERTION PASSED****')
