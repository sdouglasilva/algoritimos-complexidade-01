#Simulando um banco de dados usando uma lista
users_db = []

#Criando uma função para adicionar usuarios ao banco de dados:
def add_user_to_db(user):
  users_db.append(user)
  return user

def get_users_from_db():
  return users_db
