import json

jsondata = '{"name": "prashant","datatype": ["Int","String","List"]}'
print(jsondata)
print(type(jsondata))

jsondata1 = json.loads(jsondata)
print(type(jsondata1))
print(jsondata1)

print(jsondata1['datatype'])

jsondata2 = jsondata1['datatype']
print(type(jsondata2))
print(jsondata2)
print(jsondata2[0])