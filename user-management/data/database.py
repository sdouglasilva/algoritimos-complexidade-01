# Simulação de um banco de dados usando uma lista
users_db = []

def add_user_to_db(user):
    users_db.append(user)

def get_users_from_db():
    return users_db
