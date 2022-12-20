import json

with open("D:\PythonExercise\PythonLearning\parse_data.json") as f4:
    f5 = json.load(f4)
    print(f5)
    for i in f5["courses"]:
        if i["title"] == "PYTHON":
            print(i["details"])

