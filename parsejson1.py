import json

jsontest4 = '{"name": "prashant","datatype": ["Int","String","List"]}'
jsontest5 = json.loads(jsontest4)

print(jsontest5['datatype'][0:2])
