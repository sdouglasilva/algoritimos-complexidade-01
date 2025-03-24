from data.database import add_user_to_db, get_users_from_db
from services.utils import validate_email

def create_user(name, email):
    """Cria um novo usuário e o adiciona ao 'banco de dados'."""
    if not validate_email(email):
        return "Erro: E-mail inválido!"
    
    user = {"name": name, "email": email}
    add_user_to_db(user)
    return f"Usuário {name} cadastrado com sucesso!"

def list_users():
    """Lista todos os usuários cadastrados."""
    users = get_users_from_db()
    if not users:
        return "Nenhum usuário cadastrado."
    
    return "\n".join([f"Nome: {u['name']}, E-mail: {u['email']}" for u in users])
