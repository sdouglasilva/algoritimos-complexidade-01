### Projeto criado para exemplificar conceitos de Programação Estruturada e TopDown

```user_management/
│── main.py              # Ponto de entrada do programa
│── services/
│   ├── user_service.py  # Funções de manipulação de usuários
│   ├── utils.py         # Funções auxiliares
│── data/
│   ├── database.py      # Simulação de banco de dados
│── tests/
│   ├── test_users.py    # Testes unitários
```

## 📌 Como esse código reflete os conceitos?

### ✅ Programação Estruturada

- **Sequência** – O código segue um fluxo lógico claro.
- **Decisão** – Usa `if-else` para verificar entrada do usuário.
- **Repetição** – O menu principal roda dentro de um `while True`.
- **Modularização** – Funções separadas para cada funcionalidade.

---

### ✅ Abordagem Top-Down

1. **Decomposição do problema**  
   Primeiramente, definimos o sistema geral (gestão de usuários).
   
2. **Divisão em módulos**  
   Criamos arquivos para separar lógica, banco de dados e utilidades.
   
3. **Implementação dos detalhes**  
   Criamos funções específicas para validar, criar e listar usuários.

---

## 🚀 Rodando o Projeto

Para rodar o programa, execute o seguinte comando no terminal:

```bash
python main.py

