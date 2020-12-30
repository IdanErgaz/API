import requests, jsonpath, json

#creating a new resource

url="https://reqres.in/api/users"
#Read Input json file
file= open("E:\\TestFiles\\API\\createUser.json", 'r')
json_input=file.read()
requests_json=json.loads(json_input)
print("This is the user I want to add:", requests_json)

#Make POST request  with json_input body
response=requests.post(url, requests_json)
print(response.content)
#Validating Response Code should be 201
assert response.status_code==201

#featch ALLheaader from resonsepe
print("ALL headers:", response.headers)
#fetch specific header
print(response.headers.get('Content-Length'))

#Parse response to JSON format
response_json=json.loads(response.text)
#Pick ID using json path
id=jsonpath.jsonpath(response_json, 'id')
print("UserId:",id[0])
