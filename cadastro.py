import json

usuarios = []

# =========================
# FUNÇÕES DE ARQUIVO
# =========================

def salvar():
    with open("usuarios.json", "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

def carregar():
    global usuarios
    try:
        with open("usuarios.json", "r", encoding="utf-8") as f:
            usuarios = json.load(f)
    except:
        usuarios = []

# =========================
# FUNÇÕES DO SISTEMA
# =========================

def menu():
    print("\n=== SISTEMA DE CADASTRO ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Editar usuário")
    print("4 - Deletar usuário")
    print("0 - Sair")

def cadastrar():
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()

    if not nome or not email:
        print("Nome e email são obrigatórios!")
        return

    usuarios.append({"nome": nome, "email": email})
    salvar()
    print("✅ Usuário cadastrado com sucesso!")

def listar():
    if not usuarios:
        print("⚠️ Nenhum usuário cadastrado.")
        return

    print("\n--- LISTA DE USUÁRIOS ---")
    for i, u in enumerate(usuarios):
        print(f"{i} - {u['nome']} ({u['email']})")

def obter_indice():
    try:
        i = int(input("ID do usuário: "))
        if i < 0 or i >= len(usuarios):
            print("❌ ID inválido!")
            return None
        return i
    except:
        print("❌ Digite um número válido!")
        return None

def editar():
    listar()
    i = obter_indice()
    if i is None:
        return

    nome = input("Novo nome: ").strip()
    email = input("Novo email: ").strip()

    if nome:
        usuarios[i]["nome"] = nome
    if email:
        usuarios[i]["email"] = email

    salvar()
    print("✏️ Usuário atualizado!")

def deletar():
    listar()
    i = obter_indice()
    if i is None:
        return

    confirm = input("Tem certeza que deseja deletar? (s/n): ").lower()
    if confirm == "s":
        usuarios.pop(i)
        salvar()
        print("🗑️ Usuário removido!")
    else:
        print("Operação cancelada.")

# =========================
# PROGRAMA PRINCIPAL
# =========================

def main():
    carregar()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            editar()
        elif opcao == "4":
            deletar()
        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    main()