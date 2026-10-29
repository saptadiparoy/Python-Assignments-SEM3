import csv
import json

with open("stud_data.csv", "w") as file:
    writer = csv.writer(file)

    writer.writerow (["rollno", "name", "class"])

    data = [[101, "abc", 2], [102, "xyz", 3], [103, "mno", 2]]

    writer.writerows(data)



with open("stud_data.csv", "r") as file:
    r = csv.DictReader(file)
    data = list(r)

with open ("out_stud_data.json", "w") as file:
    json.dump(data, file)