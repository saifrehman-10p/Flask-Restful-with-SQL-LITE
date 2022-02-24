from models.user import UserModel
from werkzeug.security import safe_str_cmp

# users =[
#    User(1,'bob','12345')
# ]
# username_mapping={u.username:u for u in users}    #u.username is being used for unique key for user and u is the user like bob itself
#                                                   # aand other u is being used to iterate over users(u.username is a unique key for u:bob in users)
# userid_mapping={u.id:u for u in users}
# username_mapping={'bob':{
#     'id': 1,
#     'username': 'bob',
#     'passowrd': '12345'
# }}
#
# userid_mapping={1:{
#     'id': 1,
#     'username': 'bob',
#     'passowrd': '12345'
# }}

def authenticate(username,password):
    user=UserModel.find_by_username(username)  #here username is the one mentioned in the method declaration and we are searching it by using method defined in User class
    print(username)
    print(password)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    user_id=payload['identity']  #unique identity loaded for the user
    return UserModel.find_by_id(user_id)