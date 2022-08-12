import requests

url="https://qanode96.ameyo.com:8443/cc/contactCenters"

for i in range(0,6):
    headers={"Content-Type":"application/json", "sessionId":"d690-62de38ac-ses-RajatAdmin-dKbO0eP0-41"}
    response=requests.post(url,data={"contactCenterName" : "cc"+str(i),"accessTemplateId":1,"description":"","userIds":"","isRoot":"","userTypes" :""},
                           headers=headers)
    print(response.text)