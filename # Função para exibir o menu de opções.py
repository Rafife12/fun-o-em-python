# Função para exibir o menu de opções
def exibir_menu():
    print("\n---- Sistema de Cadastro ----")
    print("1. Cadastrar usuário")
    print("2. Consultar usuário")
    print("3. Listar todos os usuários")
    print("4. Sair")
    return input("Escolha uma opção: ")

# Função para cadastrar um usuário
def cadastrar_usuario(usuarios):
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    senha = input("Digite a senha: ")

    # Verificando se o e-mail já existe
    if email in usuarios:
        print("E-mail já cadastrado!")
    else:
        # Corrigido: Utilizar chaves {} para criar o dicionário com as informações
        usuarios[email] = {
            'nome': nome,
            'senha': senha
        }
        print("Usuário cadastrado com sucesso!")

# Função para consultar um usuário
def consultar_usuario(usuarios):
    email = input("Digite o e-mail do usuário: ")

    if email in usuarios:
        usuario = usuarios[email]
        print(f"Nome: {usuario['nome']}")
        print(f"E-mail: {email}")
        print(f"Senha: {'*' * len(usuario['senha'])}")  # Mostrando a senha como asteriscos
    else:
        print("Usuário não encontrado.")

# Função para listar todos os usuários
def listar_usuarios(usuarios):
    if usuarios:
        print("\n---- Lista de Usuários ----")
        for email, dados in usuarios.items():
            print(f"Nome: {dados['nome']}, E-mail: {email}")
    else:
        print("Nenhum usuário cadastrado.")

# Função principal
def main():
    usuarios = {}
    while True:
        opcao = exibir_menu()
        
        if opcao == '1':
            cadastrar_usuario(usuarios)
        elif opcao == '2':
            consultar_usuario(usuarios)
        elif opcao == '3':
            listar_usuarios(usuarios)
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()
