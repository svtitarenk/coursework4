import os
from config import ROOT_DIR
from pathlib import Path

file_path = os.path.join(ROOT_DIR, 'data', 'operations.json')





if __name__ == "__main__":
    pass

    # class Student:
    #     def __init__(self, name, age):
    #         self.name = name
    #         self.age = age
    #
    #     def to_dict(self):
    #         return {"name": self.name, "age": self.age}
    #
    #
    # students = [Student(name="Alice", age=20), Student(name="Bob", age=22), Student(name="Charlie", age=23)]
    # students_dict_list = [student.to_dict() for student in students]