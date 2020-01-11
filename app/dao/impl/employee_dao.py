import boto3
from dao.base.dynamodb import DynamoDAO
from models.employees import Employee, EmployeeList


class EmployeeDAO(DynamoDAO):
    TABLE_NAME = 'Employees'

    def get_employee(self, employee_id:str) -> Employee:
        response = self.table.get_item(Key={'employee_id': employee_id})
        return Employee(**response['Item'])
    
    def list_employees(self) -> list:
        response = self.table.scan(Limit=100)

        pagination_key = response.get('LastEvaluatedKey', None)
        employees = [Employee(**employee_dict) for employee_dict in response['Items']]

        return EmployeeList(**{'employees': employees, 'pagination_key': pagination_key})
    
    def patch_employee(self, employee:Employee) -> Employee:
        count = 0
        employee_patch = []

        for key, val in employee.to_dict().items():
            if key == 'employee_id':
                continue
            
            if val is not None:
                employee_patch.append({
                    "key": key,
                    "name": "key_%s" % str(count),
                    "value": val
                })
                count += 1        

        update_expression = "SET " + ", ".join(map(lambda x: "#%s = :%s" % (x['name'], x['name']), employee_patch))
        update_attribute_values = {':' + e['name']: e['value'] for e in employee_patch}
        update_attribute_names = {'#' + e['name']: e['key'] for e in employee_patch}

        self.table.update_item(
            Key={'employee_id': employee.employee_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=update_attribute_values,
            ExpressionAttributeNames=update_attribute_names
        )

        response = self.table.get_item(
            Key={'employee_id': employee.employee_id}
        )

        employee = Employee(**response['Item'])
