from functools import reduce
from src.classes.student import Student, StudentSerializer
from src.classes.tree import Tree
from src.services.algsearch import ListSearch, TreeSearch


def lab1():

    students = [Student().read(student) for student in StudentSerializer.serialize('./data/students.json')]

    tree = Tree()
    [tree.insert(student.__dict__['name']) for student in students]

    ListSearch.lineal_search(students, 'name', 'Alva Bauser')
    students.sort(key=lambda item: item.name)
    ListSearch.lineal_search(students, 'name', 'Alva Bauser')
    ListSearch.binary_search(students, 'name', 'Alva Bauser')
    ListSearch.fibbonachi_search(students, 'name', 'Alva Bauser')
    students.sort(key=lambda item: reduce(lambda x, y: x + y, [ord(char) for char in item.name]))
    ListSearch.interpolar_search(students, 'name', 'Alva Bauser')
    TreeSearch.bintree_linear_search(tree, 'Alva Bauser')
    TreeSearch.recursive_tree_search(tree, 'Alva Bauser')

