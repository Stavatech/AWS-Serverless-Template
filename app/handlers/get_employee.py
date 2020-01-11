from utils.decorators import lambda_handler


@lambda_handler
def get_employee(event, context):
    employee_id = event['pathParameters']['employee_id']
    
    employee = context.config.employee_dao.get_employee(employee_id)

    return {
        "statusCode": 200,
        "body":employee.to_JSON()
    }
