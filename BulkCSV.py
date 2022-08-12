import csv

header = ["Name", "Team", "Designation"]
with open("bulkcsv.csv", "w") as outfile:
    a= csv.DictWriter(outfile, fieldnames=header)

    for i in range(0, 1):
        a.writerow([{"Name":"Rajat"+str(i),"Team":"Dev"+str(i),"Designation":"SDE1"+str(i)}])



