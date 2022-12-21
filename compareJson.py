import json

with open("D:\PythonExercise\PythonLearning\parse_data.json") as f1:
    f2 = json.load(f1)
    with open("D:\PythonExercise\PythonLearning\parse_data1.json") as f3:
        f4 = json.load(f3)
        print(f2 == f4)
        assert f2 == f4