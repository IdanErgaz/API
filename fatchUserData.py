import requests
import json
import jsonpath
#API url
url="https://reqres.in/api/users?page=2"

#SEND REQUEST---check status
response=requests.get(url)
print(response)
print("")
#display response content
print(response.content)
#display header
print(response.headers)

#parse response to json format
json_response=json.loads(response.text)
print(json_response)

#fetch value using json path
pages=jsonpath.jsonpath(json_response, 'total_pages') #return a LIST
print("Pages:", pages[0])
assert  pages[0]==2
per_page=jsonpath.jsonpath(json_response, 'per_page')
print("PerPage:", per_page[0])
supports=jsonpath.jsonpath(json_response, 'support')
print(supports)
firstName=jsonpath.jsonpath(json_response, 'data[0].first_name')
print("first name:", firstName)