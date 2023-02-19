from typing import Self


class Student():

    def __init__(self, id=None, name=None, department=None, birthday=None, admission=None) -> None:
        self.id = id
        self.name = name
        self.department = department
        self.birthday = birthday
        self.admission = admission

    def copy(self, student: Self) -> Self:
        self.id = student.id
        self.name = student.name
        self.department = student.department
        self.birthday = student.birthday
        self.admission = student.admission
        return self

    def __eq__(self, __o: object) -> bool:
        return True if self is __o else False

    def read(self, student: dict[str, str]) -> Self:
        if 'id' in student:
            self.id = student['id']
        if 'name' in student:
            self.name = student['name']
        if 'department' in student:
            self.department = student['department']
        if 'birthday' in student:
            self.birthday = student['birthday']
        if 'admission' in student:
            self.admission = student['admission']
        return self

    def print(self):
        print(f"id: {self.id}, 'name': {self.name}, 'department: {self.department}, 'birthday': {self.birthday}, 'admission': {self.admission}")
