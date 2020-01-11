from models import SerializableObject


class Employee(SerializableObject):
    def __init__(self, employee_id:str, id_number:str=None, last_name:str=None, first_names:str=None, role:str=None,
                    date_of_birth:str=None):
        self.employee_id = employee_id
        self.id_number = id_number
        self.last_name = last_name
        self.first_names = first_names
        self.role = role
        self.date_of_birth = date_of_birth


class EmployeeList(SerializableObject):
    def __init__(self, employees:list, pagination_key:str):
        self.employees = [employee.__dict__ for employee in employees]
        self.pagination_key = pagination_key
