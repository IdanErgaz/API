import jsonpath, json, requests

url="https://reqres.in/api/users/2"


#put should return 200 code

#read the UPDATED json file with the updated fields
file= open("E:\\TestFiles\\API\\createUser.json", 'r')
json_input=file.read()
request_json=json.loads(json_input)

#Make a PUT request
response=requests.put(url, request_json)

#Validation response code
assert response.status_code==200

#Parse response Content
json_response=json.loads(response.text)
#I want to fetch
updated_li=jsonpath.jsonpath(json_response, 'updatedAt')
print(updated_li[0])