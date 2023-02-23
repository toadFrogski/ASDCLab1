import json
from src.classes.student import Student
from src.classes.tree import Tree
from src.services.algsearch import ListSearch, TreeSearch
from functools import reduce


def lab1():

    students = []
    with open('data/students.json', 'r') as f:
        for item in json.load(f):
            student = Student()
            students.append(student.read(item))

    tree = Tree()
    for student in students:
        tree.insert(student.__dict__['name'])

    ListSearch.lineal_search(students, 'name', 'Alva Bauser')
    students.sort(key=lambda item: item.name)
    ListSearch.lineal_search(students, 'name', 'Alva Bauser')
    ListSearch.binary_search(students, 'name', 'Alva Bauser')
    ListSearch.fibbonachi_search(students, 'name', 'Alva Bauser')
    students.sort(key=lambda item: reduce(lambda x, y: x + y, [ord(char) for char in item.name]))
    ListSearch.interpolar_search(students, 'name', 'Alva Bauser')
    TreeSearch.bintree_linear_search(tree, 'Alva Bauser')
    TreeSearch.recursive_tree_search(tree, 'Alva Bauser')

