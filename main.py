from Data.connect import Connection
from View.Login.login import Login

connection = Connection()

login = Login(connection)
login.mainloop()
