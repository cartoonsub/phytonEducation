import json

student1 = {'name': 'John', 'age': '20', 'city': 'New York', 'scores': [1, 2, 3, 4, 5]}
student2 = {'name': 'Mary', 'age': '21', 'city': 'London', 'scores': [1, 2, 3, 4, 5]}

data = [student1, student2]
dataJson = (json.dumps(data, indent=4, sort_keys=True))

with open('C:\\phytonProjects\\phytonEducation\\firstStep\\part3Request\\static\\jsonWrite.json', 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)

dataAgain = json.loads(dataJson)
print(dataAgain[0]['scores'])
print(sum(dataAgain[0]['scores']))

with open('C:\\phytonProjects\\phytonEducation\\firstStep\\part3Request\\static\\jsonWrite.json', 'r') as f:
    print(json.load(f))