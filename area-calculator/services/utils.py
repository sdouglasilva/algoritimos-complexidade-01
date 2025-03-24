import re

def validate_email(email):
  pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-0-9]+\.[a-zA-0-9]+$"
  return re.match(pattern, email)is not None



### Um pouco sobre regex

import re

# String a ser testada
text = "cA-O9-M9-2"

# Expressão regular
pattern = r"[a-zA-Z0-9]+"

# Verificar cada caractere manualmente
for char in text:
    ascii_code = ord(char)  # Obtém o código ASCII do caractere
    in_lowercase = 97 <= ascii_code <= 122
    in_uppercase = 65 <= ascii_code <= 90
    in_digits = 48 <= ascii_code <= 57

    print(f"Caractere: {char} | ASCII: {ascii_code} | "
          f"{'✅ Aceito' if in_lowercase or in_uppercase or in_digits else '❌ Rejeitado'}")

# Testar regex no Python
match = re.match(pattern, text)

print("\nResultado final do regex:", "✅ Match encontrado!" if match else "❌ String inválida!")
