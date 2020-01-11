from utils.decorators import lambda_handler


@lambda_handler
def list_employees(event, context):
    employee_list = context.config.employee_dao.list_employees()

    return {
        "statusCode": 200,
        "body": employee_list.to_JSON()
    }
