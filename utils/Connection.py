import psycopg2

class Connection:
    instance: psycopg2 = None

    def __init__(self, _host, _database, _user, _password):
            self.instance = psycopg2.connect(host=_host, database=_database, user=_user, password=_password)


