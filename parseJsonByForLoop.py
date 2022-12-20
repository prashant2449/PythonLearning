import json

with open("D:\PythonExercise\PythonLearning\parse_data.json") as f2:
    f3 = json.load(f2)
    print(f3)
    for i in f3["courses"]:
        if i["title"] == "CYPRESS":
            print(i["price"])