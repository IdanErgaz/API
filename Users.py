import json, jsonpath, requests
import time

addUser_api="http://thetestingworldapi.com/api/studentsDetails"
file=open("E:\\TestFiles\\API\\addUser.json")
input=file.read()
request_json=json.loads(input) #parse input to JSON
response=requests.post(addUser_api, request_json) #api request POST for user creation
print(response.text)
assert response.status_code==201
print("Assert of adding a new user - pass successfully!")
response_json=json.loads(response.text)
id=jsonpath.jsonpath(response_json, 'id')
id1=str(id[0])

#Get student details
student_api="http://thetestingworldapi.com/api/studentsDetails/"+str(id1)
userRespond=requests.get(student_api)
assert userRespond.status_code==200
print("assert of reading the new added user details - pass!")
print(userRespond.content)

#Add technicals skills to the student
addSkills_api="http://thetestingworldapi.com/api/technicalskills/"+str(id1)
file=open("E:\\TestFiles\\API\\addSkill.json")
input=file.read()
input_jason=json.loads(input)
input_jason['id']=id1
input_jason['st_id']=id1
response_skill=requests.post(addSkills_api, input_jason)
print(response_skill.status_code)
assert response_skill.status_code==200
print("skill was added successfully!")

#Get the Final student details
details_api="http://thetestingworldapi.com/api/FinalStudentDetails/"+ id1
detailsRespond=requests.get(details_api)
print(detailsRespond.status_code)
time.sleep(1)
print(detailsRespond.content)

#delete the user
delete_api="http://thetestingworldapi.com/api/Students/"+id1
respondDelete=requests.delete(delete_api)
print(respondDelete.status_code, respondDelete.content)#due to permissions we can't delete users

#delete user details
deleteUserDetails_api="http://thetestingworldapi.com/api/studentsDetails/" + id1
responseDeleteUserDetails=requests.delete(deleteUserDetails_api)
print(responseDeleteUserDetails.status_code, responseDeleteUserDetails.content)

#get user address
address_api="http://thetestingworldapi.com/api/addresses/"+id1
address_response=requests.get(address_api)
print(address_response.content, "code:", address_response.status_code)

#post user address
setAddress_api="http://thetestingworldapi.com/api/addresses"
file=open("E:\\TestFiles\\API\\setAddress.json", 'r')
input=file.read()
input_json2=json.loads(input)
SetAddressRespond=requests.post(setAddress_api, input_json2)
print(SetAddressRespond.content)