class LoginController:

    @staticmethod
    def login(connection, username, password):
        connection.cur.execute("SELECT * FROM users WHERE users.username=?", [username])
        user = connection.cur.fetchall()
        if len(user) > 0:
            if user[0][2] == password:
                return {'status': 200, 'message': "Login successful!"}
            else:
                return {'status': 401, 'message': "Incorrect password!"}
        else:
            return {'status': 401, 'message': "User does not exist!"}
