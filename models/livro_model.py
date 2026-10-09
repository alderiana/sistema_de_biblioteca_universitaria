import psycopg2

class Livro:
    def __init__(self):
        try:
            self.conexao = psycopg2.connect(
                host="localhost",   
                database="biblioteca_universitaria",
                user="postgres",
                password="1234"
            )
        except psycopg2.Error as e:
            print(f"\nErro ao conectar ao banco: {e}")

    def cadastrar_livro(self, titulo, ano_publicacao, id_autor):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "INSERT INTO livro (titulo, ano_publicacao, id_autor) VALUES (%s, %s, %s)", 
                (titulo, ano_publicacao, id_autor)
            )
            self.conexao.commit()
            cursor.close()
        except psycopg2.Error as e:
            print(f"\nErro ao cadastrar livro: {e}")

    def listar_livro(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("""
                SELECT l.id, l.titulo, l.ano_publicacao, a.nome 
                FROM livro l
                LEFT JOIN autor a ON l.id_autor = a.id
                ORDER BY l.id
            """)
            livros = cursor.fetchall()
            cursor.close()
            return livros
        except psycopg2.Error as e:
            print(f"\nErro ao listar livros: {e}")
            return []

    def atualizar_livro(self, titulo, ano_publicacao, id_autor, id):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "UPDATE livro SET titulo = %s, ano_publicacao = %s, id_autor = %s WHERE id = %s", 
                (titulo, ano_publicacao, id_autor, id)
            )
            self.conexao.commit()
            cursor.close()
        except psycopg2.Error as e:
            print(f"\nErro ao atualizar livro: {e}")

    def excluir_livro(self, id):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM livro WHERE id = %s", (id,))
            self.conexao.commit()
            cursor.close()
        except psycopg2.Error as e:
            print(f"\nErro ao deletar livro: {e}")
