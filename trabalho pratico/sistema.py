import csv
import getpass

USUARIOS_ARQUIVO = 'usuarios.csv'
PRODUTOS_ARQUIVO = 'produtos.csv'

# ----------------------------- Funções de arquivo -----------------------------
def carregar_usuarios():
    usuarios = []
    try:
        with open(USUARIOS_ARQUIVO, newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                usuarios.append(linha)
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado. Criando novo...")
    return usuarios

def salvar_usuarios(usuarios):
    with open(USUARIOS_ARQUIVO, 'w', newline='', encoding='utf-8') as f:
        campos = ['nome', 'login', 'senha', 'tipo']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(usuarios)

# ----------------------------- Sistema de Login -----------------------------
def login(usuarios):
    login_input = input("Login: ")
    senha_input = getpass.getpass("Senha: ")
    for u in usuarios:
        if u['login'] == login_input and u['senha'] == senha_input:
            print(f"Bem-vindo, {u['nome']}! Tipo de usuário: {u['tipo']}")
            return u
    print("Login ou senha incorretos.")
    return None

# ----------------------------- CRUD Usuários -----------------------------
def criar_usuario(usuarios):
    nome = input("Nome: ")
    login = input("Login: ")
    senha = input("Senha: ")
    tipo = input("Tipo (gerente/funcionario/cliente): ").lower()

    if any(u['login'] == login for u in usuarios):
        print("Erro: Login já existe.")
        return

    novo_usuario = {'nome': nome, 'login': login, 'senha': senha, 'tipo': tipo}
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    print("Usuário criado com sucesso!")

def listar_usuarios(usuarios):
    print("\n--- Lista de Usuários ---")
    for u in usuarios:
        print(f"Nome: {u['nome']}, Login: {u['login']}, Tipo: {u['tipo']}")

def atualizar_usuario(usuarios):
    login = input("Informe o login do usuário a ser atualizado: ")
    for u in usuarios:
        if u['login'] == login:
            print(f"Usuário encontrado: {u['nome']}")
            u['nome'] = input("Novo nome (pressione Enter para manter): ") or u['nome']
            u['senha'] = input("Nova senha (pressione Enter para manter): ") or u['senha']
            u['tipo'] = input("Novo tipo (gerente/funcionario/cliente): ") or u['tipo']
            salvar_usuarios(usuarios)
            print("Usuário atualizado com sucesso!")
            return
    print("Usuário não encontrado.")

def deletar_usuario(usuarios, usuario_logado):
    login = input("Informe o login do usuário a ser removido: ")
    for u in usuarios:
        if u['login'] == login:
            if usuario_logado['tipo'] == 'gerente':
                if u['tipo'] == 'gerente':
                    print("Erro: Um gerente não pode deletar outro gerente.")
                    return
            elif usuario_logado['tipo'] == 'funcionario':
                if u['tipo'] != 'cliente':
                    print("Erro: Funcionário só pode deletar clientes.")
                    return
            elif usuario_logado['tipo'] == 'cliente':
                print("Erro: Cliente não tem permissão para deletar usuários.")
                return

            confirmar = input(f"Tem certeza que deseja remover '{u['login']}'? (s/n): ").lower()
            if confirmar != 's':
                print("Remoção cancelada.")
                return

            usuarios.remove(u)
            salvar_usuarios(usuarios)
            print("Usuário removido com sucesso!")
            return
    print("Usuário não encontrado.")

def ordenar_usuarios_por_nome(usuarios):
    ordenados = sorted(usuarios, key=lambda u: u['nome'].lower())
    listar_usuarios(ordenados)

def ordenar_usuarios_por_tipo(usuarios):
    ordenados = sorted(usuarios, key=lambda u: u['tipo'].lower())
    listar_usuarios(ordenados)

# ----------------------------- CRUD Produtos -----------------------------
def carregar_produtos():
    produtos = []
    try:
        with open(PRODUTOS_ARQUIVO, newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                linha['preco'] = float(linha['preco'])
                linha['quantidade'] = int(linha['quantidade'])
                produtos.append(linha)
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado. Criando novo...")
    return produtos

def salvar_produtos(produtos):
    with open(PRODUTOS_ARQUIVO, 'w', newline='', encoding='utf-8') as f:
        campos = ['codigo', 'nome', 'preco', 'quantidade']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(produtos)

def criar_produto(produtos):
    codigo = input("Código do produto: ")
    if any(p['codigo'] == codigo for p in produtos):
        print("Erro: Código já existe.")
        return
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    produtos.append({'codigo': codigo, 'nome': nome, 'preco': preco, 'quantidade': quantidade})
    salvar_produtos(produtos)
    print("Produto criado com sucesso!")

def atualizar_produto(produtos):
    codigo = input("Informe o código do produto a ser atualizado: ")
    for p in produtos:
        if p['codigo'] == codigo:
            p['nome'] = input("Novo nome (pressione Enter para manter): ") or p['nome']
            novo_preco = input("Novo preço (pressione Enter para manter): ")
            p['preco'] = float(novo_preco) if novo_preco else p['preco']
            nova_qtd = input("Nova quantidade (pressione Enter para manter): ")
            p['quantidade'] = int(nova_qtd) if nova_qtd else p['quantidade']
            salvar_produtos(produtos)
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado.")

def deletar_produto(produtos):
    codigo = input("Informe o código do produto a ser removido: ")
    for p in produtos:
        if p['codigo'] == codigo:
            confirmar = input(f"Tem certeza que deseja remover o produto '{p['nome']}' (código {p['codigo']})? (s/n): ").lower()
            if confirmar != 's':
                print("Remoção cancelada.")
                return
            produtos.remove(p)
            salvar_produtos(produtos)
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado.")

def ordenar_produtos_por_nome(produtos):
    ordenados = sorted(produtos, key=lambda p: p['nome'].lower())
    listar_produtos(ordenados)

def ordenar_produtos_por_preco(produtos):
    ordenados = sorted(produtos, key=lambda p: p['preco'])
    listar_produtos(ordenados)

def ordenar_produtos_por_codigo(produtos):
    ordenados = sorted(produtos, key=lambda p: p['codigo'])
    listar_produtos(ordenados)

def listar_produtos(produtos):
    print("\n--- Produtos Disponíveis ---")
    for p in produtos:
        print(f"Código: {p['codigo']}, Nome: {p['nome']}, Preço: R${p['preco']:.2f}, Quantidade: {p['quantidade']}")

def menu_produtos():
    produtos = carregar_produtos()
    while True:
        print("\n--- MENU PRODUTOS ---")
        print("1. Adicionar produto")
        print("2. Atualizar produto")
        print("3. Deletar produto")
        print("4. Ordenar por nome")
        print("5. Ordenar por preço")
        print("6. Ordenar por código")
        print("7. Listar todos")
        print("8. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_produto(produtos)
        elif opcao == '2':
            atualizar_produto(produtos)
        elif opcao == '3':
            deletar_produto(produtos)
        elif opcao == '4':
            ordenar_produtos_por_nome(produtos)
        elif opcao == '5':
            ordenar_produtos_por_preco(produtos)
        elif opcao == '6':
            ordenar_produtos_por_codigo(produtos)
        elif opcao == '7':
            listar_produtos(produtos)
        elif opcao == '8':
            break
        else:
            print("Opção inválida.")

# ----------------------------- Menus por Tipo -----------------------------
def menu_gerente(usuario_logado, usuarios):
    while True:
        print("\n--- MENU GERENTE ---")
        print("1. Gerenciar usuários")
        print("2. Gerenciar produtos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            menu_usuarios(usuario_logado, usuarios)
        elif opcao == '2':
            menu_produtos()
        elif opcao == '3':
            return  # Logout
        else:
            print("Opção inválida.")

def menu_funcionario(usuario_logado):
    while True:
        print("\n--- MENU FUNCIONÁRIO ---")
        print("1. Gerenciar produtos")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            menu_produtos()
        elif opcao == '2':
            return  # Logout
        else:
            print("Opção inválida.")

def menu_cliente():
    produtos = carregar_produtos()
    print("\n--- LISTA DE PRODUTOS ---")
    listar_produtos(produtos)

def menu_usuarios(usuario_logado, usuarios):
    while True:
        print("\n--- MENU USUÁRIOS ---")
        print("1. Criar usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("5. Ordenar por nome")
        print("6. Ordenar por tipo")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_usuario(usuarios)
        elif opcao == '2':
            listar_usuarios(usuarios)
        elif opcao == '3':
            atualizar_usuario(usuarios)
        elif opcao == '4':
            deletar_usuario(usuarios, usuario_logado)
        elif opcao == '5':
            ordenar_usuarios_por_nome(usuarios)
        elif opcao == '6':
            ordenar_usuarios_por_tipo(usuarios)
        elif opcao == '7':
            break
        else:
            print("Opção inválida.")

# ----------------------------- Execução Principal -----------------------------
if __name__ == '__main__':
    while True:
        usuarios = carregar_usuarios()
        usuario_logado = login(usuarios)
        if usuario_logado:
            tipo = usuario_logado['tipo']
            if tipo == 'gerente':
                print("\n🔐 Bem-vindo ao sistema, gerente! Você tem acesso completo.")
                menu_gerente(usuario_logado, usuarios)
            elif tipo == 'funcionario':
                print("\n📦 Bem-vindo, funcionário! Acesse e gerencie os produtos.")
                menu_funcionario(usuario_logado)
            elif tipo == 'cliente':
                print("\n🛒 Bem-vindo, cliente! Confira os produtos disponíveis.")
                menu_cliente()
            else:
                print("Tipo de usuário inválido.")
        else:
            opcao = input("Deseja tentar novamente? (s/n): ").lower()
            if opcao != 's':
                break
