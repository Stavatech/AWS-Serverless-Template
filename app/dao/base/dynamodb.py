class DynamoDAO(object):
    TABLE_NAME = 'TABLE_NAME'

    def __init__(self, db_client):
        self.db_client = db_client
        self.table = db_client.Table(self.TABLE_NAME)