import pytest, json, jsonpath, requests

def test_addNew_data():
    API_url="http://thetestingworldapi.com/api/studentsDetails"
    f= open('E:/TestFiles/API/requestJson.json', 'r')
    request_json=json.loads(f.read())
    response=requests.post(API_url, request_json)
    print(response.text)
    print(response.status_code)
    id=jsonpath.jsonpath(response.json(), 'id')
    print("ID:", id[0])

    tech_url="http://thetestingworldapi.com/api/technicalskills"
    f= open('E:/TestFiles/API/techDetails.json', 'r')
    request_json=json.loads(f.read())
    request_json['id']=id[0]
    request_json['st_id']=int(id[0])
    response=requests.post(tech_url, request_json)
    print(response.text)

    address_api="http://thetestingworldapi.com/api/addresses"
    f = open('E:/TestFiles/API/address.json', 'r')
    request_json = json.loads(f.read())
    request_json['stId']=id[0]
    response = requests.post(address_api, request_json)
    print(response.content)
    #
    # finalDetails1="http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    # response=requests.get(finalDetails1)
    # print(response.text)

