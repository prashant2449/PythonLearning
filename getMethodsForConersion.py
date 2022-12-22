import requests
import json

json_response = requests.get('http://preprod-payment.nyk00-int.network/payment/info/availablePaymentMethodsForConversion',
             params={'deviceType': 'MSITE', 'domain': 'nykaa'})

print(json_response.status_code)
print(json_response.headers)

parsed_json_response = json_response.json()
