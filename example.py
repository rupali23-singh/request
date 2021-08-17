import requests
import json 
res=requests.get("http://saral.navgurukul.org/api/courses")
course=json.loads(res.text)
print(course)
id=[]
index=0
while index<len(course):
    print(course[index])







