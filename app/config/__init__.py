import boto3
from dao.impl.employee_dao import EmployeeDAO


dynamodb = boto3.resource('dynamodb')
employee_dao = EmployeeDAO(dynamodb)
