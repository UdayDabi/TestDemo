class LoginException(Exception):

    def __int__(self, msg):
        super().__int__(msg)


Login_id = "Admin"
Password = "Admin"

try:
    if Login_id == 'Admin' and Password == 'Amin':
        print("Valid User")

    else:
        raise LoginException("Invalid LoginId and Password.....plz Try again")


except ZeroDivisionError as e:
    print('Zero divison', e)

except Exception as e:
    print('LoginException', e)