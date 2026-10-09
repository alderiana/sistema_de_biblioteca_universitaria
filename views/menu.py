class BibliotecaView:
    @staticmethod
    def menu_principal():
        print("\n===== MENU PRINCIPAL =====")
        print("1. Gerenciar autor")
        print("2. Gerenciar livro")
        print("3. Sair")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    @staticmethod
    def menu_livro():
        print("\n===== GERENCIAR LIVRO =====")
        print("1. Cadastrar livro")
        print("2. Listar livros (mostrar o nome do autor associado)")
        print("3. Atualizar livro")
        print("4. Excluir livro")
        print("5. Voltar ao menu principal")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    @staticmethod
    def cadastrar_livro():
        print("\n--- Cadastrar Novo Livro ---")
        titulo = input("Título do livro: ")
        try:
            ano = int(input("Ano de publicação: "))
            id_autor = int(input("ID do autor: "))
            return titulo, ano, id_autor
        except ValueError:
            print("\n[Erro] Entrada inválida para números.")
            return None, None, None

    @staticmethod
    def listar_livros(livros):
        if not livros:
            print("\nNenhum livro cadastrado.")
        else:
            print("\n==================== LISTA DE LIVROS ====================")
            for l in livros:
                print(f"ID: {l[0]} | Título: {l[1]} | Ano: {l[2]} | Autor Associado: {l[3] or 'Não informado'}")
            print("=========================================================")

    @staticmethod
    def atualizar_livro():
        print("\n--- Atualizar Dados do Livro ---")
        try:
            id_livro = int(input("ID do livro que deseja atualizar: "))
            titulo = input("Novo título: ")
            ano = int(input("Novo ano de publicação: "))
            id_autor = int(input("Novo ID do autor: "))
            return titulo, ano, id_autor, id_livro
        except ValueError:
            print("\n[Erro] Entrada de dados inválida.")
            return None, None, None, None

    @staticmethod
    def excluir_livro():
        print("\n--- Excluir Livro ---")
        try:
            return int(input("ID do livro a excluir: "))
        except ValueError:
            print("\n[Erro] ID inválido.")
            return None

    @staticmethod
    def mensagem(msg):
        print(msg)
