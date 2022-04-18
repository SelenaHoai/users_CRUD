from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'users_schema'


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @property
    def fullname(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    @classmethod
    def create(cls, data: dict) -> object:
        # query string
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        # contact the DB
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        # return
        return user_id

    @classmethod
    def delete(cls, data: dict) -> object:
        # query string
        query = "DELETE FROM users WHERE id = (%(id)s);"
        # contact the DB
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        # return
        return user_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            users = []
            for user in results:
                users.append(cls(user))
            return users
        return results

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        first_row = result[0]  # get first item from result
        user_from_db = cls(first_row)
        return user_from_db

    @classmethod
    def update_one(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        # return cls(result[0])

# save || create
# get_all
# get_one
# update_one
# delete_one
