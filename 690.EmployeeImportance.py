

def findImportance(employees, id):
    employee = findEmployee(employees, id)
    if employee == None:
        return 0
    importance = employee.importance

    for i in employee.subordinates:
        importance += findImportance(employees, i)

    return importance

def findEmployee(employees, id):
    for employee in employees:
        if employee.id == id:
            return employee
    return None


class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        return findImportance(employees,id)

