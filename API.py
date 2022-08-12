import requests

a=requests.get("https://google.com",headers={"content-type":"application/json"},params={"camp_id":"3"})

#a=requests.post()
print(a.text)



