import json
from utils.decorators import lambda_handler
from models.employees import Employee


@lambda_handler
def patch_employee(event, context):
    employee_dict = json.loads(event['body'])
    input_employee = Employee(**employee_dict)

    output_employee = context.config.employee_dao.patch_employee(input_employee)
    
    return {
        "statusCode": 200,
        "body": output_employee.to_JSON(),
    }
