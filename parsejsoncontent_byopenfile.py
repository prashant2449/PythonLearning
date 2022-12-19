import json

with open("D:\\PythonExercise\\PythonLearning\\parse_data.json") as file1:
    file2 = json.load(file1)
    print(type(file2))
    print(file2)

print(file2["courses"][1]["title"])
print(file2["dashboard"]["website"])
print(file2["courses"][0]["details"]["website"])
