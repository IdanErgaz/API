import jsonpath, json, requests
#Delete a user

url="https://reqres.in/api/users/2"

response=requests.delete(url) #we should get code 204!
#fetch response code
print(response.status_code)
assert response.status_code==204
print(response.content)
