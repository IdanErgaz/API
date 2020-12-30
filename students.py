import pytest, jsonpath, json, requests

def test_getCurrentStudents():
    students_api="https://reqres.in/api/users?page=2"
    response=requests.get(students_api)
    print(response)
    assert response.status_code==200, "the response is BAD!!!" #Validate that we get the correct response code
    print(response.content)
    response_json=json.loads(response.text)
    print("#########################")
    data= jsonpath.jsonpath(response_json, 'data' )
    print(data)
    for obj in data:
        print(obj)

def test_addNewUsers():
    api_createUser="https://reqres.in/api/users"
    file=open("E:\\TestFiles\\API\\createUser.json", 'r')
    input=file.read()
    request_json=json.loads(input)
    print("this is the user I want to add:", request_json)
    response=requests.post(api_createUser, request_json)
    print("Reponse:", response)
    assert response.status_code==201
    print("response content:", response.content)
    id1=jsonpath.jsonpath(response, 'id[0]')

    #Update the user
    updateApi="https://reqres.in/api/users/"+str(id1)
    file=open("E:\\TestFiles\\API\\createUser.json", 'r')
    input=file.read()
    request_json=json.loads(input) #parse the request to json file
    respond=requests.put(updateApi, request_json)

    assert respond.status_code==200
    json_respond=json.loads(respond.text)
    userName=jsonpath.jsonpath(json_respond, 'name')
    assert userName[0]=='Idan333'

# checkUserInTheList():
    id1=jsonpath.jsonpath(response, 'id[0]')

    api_check="https://reqres.in/api/users/"+str(id1)
    response=requests.get(api_check)
    json_response = json.loads(response.text)
    print("Before Delete:", json_response)

    #Delete the user the we have created
    deleteResponse=requests.delete(api_check)
    print(deleteResponse.status_code)
    print("AfterDelete:", deleteResponse.content)
#Todo:
#get students list
#add a  new student
#verify the was adeed
#delete the  student
